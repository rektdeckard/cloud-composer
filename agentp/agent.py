import asyncio
import os
import time
import logging
import pickle
from typing import (
    Any,
    AsyncIterable,
)

from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    JobProcess,
    WorkerOptions,
    WorkerPermissions,
    cli,
    llm,
    transcription,
    stt,
)

from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import openai, deepgram, silero, rag
from googleapiclient.discovery import build


load_dotenv(dotenv_path=".env.local")
logger = logging.getLogger("voice-agent")

annoy_index = rag.annoy.AnnoyIndex.load("vdb_data")  # see build_data.py

embeddings_dimension = 1536
with open("my_data.pkl", "rb") as f:
    paragraphs_by_uuid = pickle.load(f)


# Step 1: Initialize the YouTube API client
def get_youtube_service():
    return build("youtube", "v3", developerKey=os.getenv("GOOGLE_API_KEY"))

# Step 2: Get the live chat ID for the video
def get_live_chat_id(youtube, video_id):
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    )
    response = request.execute()
    live_chat_id = response["items"][0]["liveStreamingDetails"].get("activeLiveChatId")
    return live_chat_id

# Step 3: Retrieve live chat messages
def get_live_chat_messages(youtube, live_chat_id):
    request = youtube.liveChatMessages().list(
        liveChatId=live_chat_id,
        part="snippet,authorDetails"
    )
    response = request.execute()
    return response


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()

# async def _forward_transcription(
#     stt_stream: stt.SpeechStream,
#     stt_forwarder: transcription.STTSegmentsForwarder,
# ):
#     """Forward the transcription to the client and log the transcript in the console"""
#     async for ev in stt_stream:
#         stt_forwarder.update(ev)
#         if ev.type == stt.SpeechEventType.INTERIM_TRANSCRIPT:
#             print(ev.alternatives[0].text, end="")
#         elif ev.type == stt.SpeechEventType.FINAL_TRANSCRIPT:
#             print("\n")
#             print(" -> ", ev.alternatives[0].text)


async def entrypoint(ctx: JobContext):
    # tasks = []
    # stt = deepgram.STT()
    #
    # async def transcribe_track(participant: rtc.RemoteParticipant, track: rtc.Track):
    #     audio_stream = rtc.AudioStream(track)
    #     stt_forwarder = transcription.STTSegmentsForwarder(
    #         room=ctx.room, participant=participant, track=track
    #     )
    #     stt_stream = stt.stream()
    #     stt_task = asyncio.create_task(
    #         _forward_transcription(stt_stream, stt_forwarder)
    #     )
    #     tasks.append(stt_task)
    #
    #     async for ev in audio_stream:
    #         stt_stream.push_frame(ev.frame)
    #
    #
    # @ctx.room.on("track_subscribed")
    # def on_track_subscribed(
    #     track: rtc.Track,
    #     publication: rtc.TrackPublication,
    #     participant: rtc.RemoteParticipant,
    # ):
    #     if track.kind == rtc.TrackKind.KIND_AUDIO:
    #         tasks.append(asyncio.create_task(transcribe_track(participant, track)))
    #

    async def _enrich_with_rag(agent: VoicePipelineAgent, chat_ctx: llm.ChatContext):
        # locate the last user message and use it to query the RAG model
        # to get the most relevant paragraph
        # then provide that as additional context to the LLM
        user_msg = chat_ctx.messages[-1]
        user_embedding = await openai.create_embeddings(
            input=[user_msg.content],
            model="text-embedding-3-small",
            dimensions=embeddings_dimension,
        )

        result = annoy_index.query(user_embedding[0].embedding, n=1)[0]
        paragraph = paragraphs_by_uuid[result.userdata]
        if paragraph:
            logger.info(f"enriching with RAG: {paragraph}")
            rag_msg = llm.ChatMessage.create(
                text="Context:\n" + paragraph,
                role="assistant",
            )
            # replace last message with RAG, and append user message at the end
            chat_ctx.messages[-1] = rag_msg
            chat_ctx.messages.append(user_msg)


    with open("raw_data.md", "r") as f: 
        initial_ctx = llm.ChatContext().append(
            role="system",
            text=(
                "You are a generative music bot designed to work with the musicpy Python library. "
                "Your job is to interpret the natural-language requests from users and translate "
                "them to commands to the musicpy library in order to generate beautiful music. "
                "When asked to create a song, you should only respond with Python code. "
                "The following is a subset of the documentation for the library, and you should "
                "use it to help you understand the commands you can emit: \n\n"
            ) + f.read(),
        )

    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logger.info(f"starting voice assistant for participant {participant.identity}")


    async def forwardText(agent: VoicePipelineAgent, text: str | AsyncIterable[str]):
        if isinstance(text, AsyncIterable):
            program = ""
            async for t in text:
                program += t

            print(program)
        elif isinstance(text, str):
            print(text)
        return text


    assistant = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        before_llm_cb=_enrich_with_rag,
        before_tts_cb=forwardText,
    )

    assistant.start(ctx.room, participant)

    youtube = get_youtube_service()
    
    # The agent should be polite and greet the user when it joins :)
    await assistant.say("Hey, how can I help you today?", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
            permissions=WorkerPermissions(
                can_subscribe=True,
                can_publish=True,
            ),
        ),
    )
