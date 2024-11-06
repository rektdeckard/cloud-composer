# Introduction

Musicpy is a music programming language in Python designed to write music in very handy syntax through music theory and algorithms for musicians.

Musicpy can not only compose music, but also has many algorithms in analyzing music notes, including complex chord detection based on music theory, split main melody and chords for any music and so on.

In this wiki, I am going to talk about the data structures and basic syntax of musicpy, and how to use it.

The initial purpose of why I design this language is to write music in codes with handy syntax, and the most important thing is, this language is completely designed for music theory, which means you can do anything you want in music theory when using this language.

I am trying my best to completely transform the entire music theory system into pure mathematical models (and structures) and computerized system in this project, to build a whole system of music theory that the computers could understand easily, which makes everybody can do researches in designing and developing algorithms about music theory and music itself, intellectualized analysis of music, making experimental music and so on in the world of musicpy. (and of course you can use musicpy to compose any genres of music you like, classical music, jazz, rock, pop, edm and so on)

For the data structure of musicpy, just see the data structures section.

For the basic syntax and useful functionality of musicpy, just see the basic syntax section.

For musicpy composition codes examples, just see the musicpy composition code examples section.

I added a new module called daw for musicpy in June 2021, this module can load instruments such as audio files and soundfonts files (.sf2, .sf3, .dls) and play or export audio files with musicpy, it is very easy and convenient to use.

To learn how to use this module, please refer to the musicpy daw module section.

If you want to explore more on the music analysis algorithms side with musicpy, you can see the algorithms section, this section contains the analyzing algorithms based on music theory I designed using musicpy.

# Composition Examples

Because musicpy has too many features to introduce, I will just give a simple example code of music programming in musicpy:

```python
# a nylon string guitar plays broken chords on a chord progression

guitar = (C('CM7', 3, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2 |
          C('A7sus', 2, 1/4, 1/8)^2 |
          C('Em7', 2, 1/4, 1/8)^2 | 
          C('FM7', 2, 1/4, 1/8)^2 |
          C('CM7', 3, 1/4, 1/8)@1 |
          C('AbM7', 2, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2) * 2

play(guitar, bpm=100, instrument=25)
```
This is a chapter for a quickstart and cheat sheet for musicpy, in case you find the documentation are too long and complicated to read and hard to find what you want.

# Cheat Sheet

(in case you import musicpy as `from musicpy import *`)

Note1: the chord type of muscipy has a `interval` attribute which is the list of the length of bars between the starts of each 2 adjacent notes of the chord, please don't confuse this with the music theory's interval which is a difference in pitch between 2 notes (e.g. major third, semitone). In the cheat sheet we'll use `music intervals` to denote the music theory's interval.

Note2: the default indexing is 0-based for all functions unless 1-based is mentioned.

|                        functionality                         |                     syntax (recommended)                     |                         alternatives                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                     construct a note C5                      |                           N('C5')                            |                    N('c5');  note('C', 5)                    |
|                   construct a chord Cmaj7                    |                          C('Cmaj7')                          |                    get_chord('C', 'maj7')                    |
|        construct a chord Cmaj7 with starting note C5         |                         C('C5:maj7')                         |   C('Cmaj7', pitch=5);<br/>get_chord('C', 'maj7', pitch=5)   |
|           construct a chord with notes C5, E5, G6            |                     chord('C5, E5, G6')                      | chord('c5, e5, g6');<br/>chord(['C5', 'E5', 'G6']);<br/>chord(['c5', 'e5', 'g6']);<br/>chord([N('C5'), N('E5'), N('G6')]) |
|                  construct a C major scale                   |                         S('C major')                         |                     scale('C', 'major')                      |
|                      construct a piece                       | build(track(content=C('C'), instrument=1, start_time=0),<br/>track(content=C('D'), instrument=47, start_time=1), bpm=150) | P(tracks=[C('C'), C('D')],<br/>instruments=[1, 47],<br/>start_times=[0, 1],<br/>bpm=150) |
|                      construct a track                       |      track(content=C('C'), instrument=1, start_time=0)       |                                                              |
|                construct a set of drum beats                 |             drum('K, H, H, K, S, H, H, H, t:1')              |                                                              |
|         transpose a chord/note A up/down n semitones         |                         A + n; A - n                         |                      A.up(n); A.down(n)                      |
|         raise/lower ith note of chord A n semitones          |                    A + (n, i); A - (n, i)                    |                   A.up(n, i); A.down(n, i)                   |
|     raise/lower ith to jth notes of chord A n semitones      |                 A + (n, i, j); A - (n, i, j)                 |                A.up(n, i, j); A.down(n, i, j)                |
|               concatenate chord A and chord B                |                            A \| B                            |                            A + B                             |
|    concatenate chord B after chord A with n bars interval    |                         A \| (B, n)                          |                          A + (B, n)                          |
|                add rest of n bars to chord A                 |                            A \| n                            |                          A.rest(n)                           |
|  concatenate chord A n times with interval i bars each time  |                         A \| (n, i)                          |                          A * (n, i)                          |
|                     stack chord A and B                      |                            A & B                             |                                                              |
|              stack chord B n bars after chord A              |                          A & (B, n)                          |                                                              |
|                    stack chord A n times                     |                            A & n                             |                                                              |
|     stack chord A n times with interval i bars each time     |                          A & (n, i)                          |                                                              |
|                    repeat chord A n times                    |                            A * n                             |                                                              |
|                   get ith note of chord A                    |                             A[i]                             |                                                              |
|               get ith to jth notes of chord A                |                            A[i:j]                            |                                                              |
|                 set ith note of chord A to j                 |                           A[i] = j                           |                                                              |
|              get the number of notes of chord A              |                            len(A)                            |                                                              |
|                  get the reverse of chord A                  |                              ~A                              |                         A.reverse()                          |
|             transpose chord/note A up 1 semitone             |                              +A                              |                            A.up()                            |
|            transpose chord/note A down 1 semitone            |                              -A                              |                           A.down()                           |
| set duration, interval and volume of chord A and return a new chord A |               A % (duration, interval, volume)               |              A.set(duration, interval, volume)               |
|               get the nth inversion of chord A               |                            A / n                             |                        A.inversion(n)                        |
|        invert the nth note of chord A to the highest         |                            A ^ n                             |                A / -n; A.inversion_highest(n)                |
|         invert the nth note of chord A to the lowest         |                            A @ n                             |                           A.inv(n)                           |
| form a new chord from the notes of chord A by index (1-based) |                A @ [1, 2, 3, 2, 1.1, 2, 3, 2]                |                                                              |
| form a new chord from the notes of chord A by index (1-based), increased octaves |                       A / [1, 2, 4, 3]                       |                                                              |
|           modulate chord A from scale i to scale j           |                      A.modulation(i, j)                      |                                                              |
|                  delete ith note of chord A                  |                           del A[i]                           |                                                              |
| append note i to chord A with interval j and return a new chord A |                            A + i                             |                                                              |
|           append note i to chord A with interval j           |                        A.append(i, j)                        |                                                              |
|     remove note i from chord A and return a new chord A      |                            A - i                             |                                                              |
|                  remove note i from chord A                  |                         A.remove(i)                          |                                                              |
|                  pop ith note from chord A                   |                           A.pop(i)                           |                                                              |
|     insert note j at index i with interval k to chord A      |                  A.insert(i, j, interval=k)                  |                                                              |
|                  drop n voicing of chord A                   |                          A.drops(n)                          |                                                              |
|            negative harmony of chord A at scale B            |                            A @ B                             |                    A.negative_harmony(B)                     |
|       get chord A from ith bars to jth bars (0-based)        |                         A.cut(i, j)                          |                                                              |
|      get a new chord based on changing chord A's notes       |                       A('omit 3, b9')                        |                                                              |
|           get the total length in bars of chord A            |                           A.bars()                           |                                                              |
|              get durations of notes of chord A               |                       A.get_duration()                       |                                                              |
|              get intervals of notes of chord A               |                          A.interval                          |                                                              |
|          set duration, volume and channel of note A          |               A % (duration, volume, channel)                |               A.set(duration, volume, channel)               |
| change the accidentals of note A (# to b, b to #) and return a new note |                              ~A                              |                                                              |
|            get dotted note of note A with n dots             |                         A.dotted(n)                          |                                                              |
|                    get duration of note A                    |                          A.duration                          |                                                              |
|               raise/lower scale A n semitones                |                         A + n; A - n                         |                      A.up(n); A.down(n)                      |
|         raise/lower ith note of scale A n semitones          |                    A + (n, i); A - (n, i)                    |                   A.up(n, i); A.down(n, i)                   |
|     raise/lower ith to jth notes of scale A n semitones      |                 A + (n, i, j); A - (n, i, j)                 |                A.up(n, i, j); A.down(n, i, j)                |
|                raise/lower scale A 1 semitone                |                            +A; -A                            |                       A.up(); A.down()                       |
|                  get ith degree of scale A                   |                             A[i]                             |                                                              |
|             get ith degree of scale A (1-based)              |                       A.get_degree(i)                        |                                                              |
|                   get ith triad of scale A                   |                             A(i)                             |                  A.pick_chord_by_degree(i)                   |
|                 get ith 7th chord of scale A                 |                         A(i, num=4)                          |               A.pick_chord_by_degree(i, num=4)               |
|              get ith mode of scale A (1-based)               |                            A / i                             |                        A.inversion(i)                        |
|          get chord with notes from scale A by index          |                        A @ [0, 2, 4]                         |               A.pick_chord_by_index([0, 2, 4])               |
|              get the reversed scale of scale A               |                              ~A                              |                         A.reverse()                          |
|  get a chord progression with degrees of scale A (1-based)   |                           A % 6451                           |                       A.pattern(6451)                        |
|                   get ith track of piece A                   |                             A[i]                             |                                                              |
|            get chord type of ith track of piece A            |                             A(i)                             |                         A.tracks[i]                          |
|               raise/lower piece A n semitones                |                         A + n; A - n                         |                                                              |
|         raise/lower ith track of piece A n semitones         |                     A[i] += n; A[i] -= n                     |                                                              |
|                    repeat piece A n times                    |                            A * n                             |                                                              |
|               concatenate piece A and piece B                |                            A + B                             |                            A \| B                            |
|                  stack piece A and piece B                   |                            A & B                             |                                                              |
|                 delete ith track of piece A                  |                           del A[i]                           |                                                              |
|                  get the reverse of piece A                  |                              ~A                              |                         A.reverse()                          |
|             get the number of tracks of piece A              |                            len(A)                            |                                                              |
|               append a new track n to piece A                |                         A.append(n)                          |                                                              |
|          insert a new track n at index i to piece A          |                        A.insert(i, n)                        |                                                              |
|           get the total length in bars of piece A            |                           A.bars()                           |                                                              |
|               read a MIDI file into piece type               |                          read(path)                          |                                                              |
|  write a note/chord/piece/track/drum type A to a MIDI file   |                           write(A)                           |                                                              |
|     play a note/chord/piece/track/drum type A at bpm 100     |                       play(A, bpm=100)                       |                                                              |
|                         stop playing                         |                          stopall()                           |                                                              |
|            concatenate a list of chords [A, B, C]            |                      concat([A, B, C])                       |                                                              |
| concatenate a list of chords [A, B, C] with extra interval i |                  concat([A, B, C], extra=i)                  |                                                              |
|               stack a list of chords [A, B, C]               |                 concat([A, B, C], mode='&')                  |                                                              |
|    stack a list of chords [A, B, C] with extra interval i    |             concat([A, B, C], mode='&', extra=i)             |                                                              |
|                 get note from MIDI degree i                  |                      degree_to_note(i)                       |                                                              |
|         get the degree (MIDI note number) of note A          |                           A.degree                           |                                                              |
|                 get the note name of note A                  |                            A.name                            |                                                              |
|               get the octave number of note A                |                            A.num                             |                                                              |
|              get the music intervals of chord A              |                        A.intervalof()                        |                                                              |
| construct a tempo change instance with bpm 150 and start time at 0 |                   tempo(150, start_time=0)                   |                                                              |
| construct a pitch_bend instance with value of 100 cents and start time at 0 |                pitch_bend(100, start_time=0)                 |                                                              |
| construct a pan instance with value of 100% and start time at 0 |                    pan(100, start_time=0)                    |                                                              |
| construct a volume instance with value of 100% and start time at 0 |                  volume(100, start_time=0)                   |                                                              |
|                 construct a rhythm instance                  |                 rhythm('b b 0 0 b 0 b 0', 1)                 |                                                              |
|                 generate chords from rhythm                  | get_chords_from_rhythm(C('C'), rhythm('b b 0 0 b 0 b 0', 1)) |                                                              |
|       generate arpeggios of a chord between 2 octaves        |                    arp(C('Cmaj7'), 3, 7)                     |                                                              |


# Data Structures

Musicpy is a language that allows you to express the notes, rhythms, etc. of a piece of music in a very simple syntax, and can be easily exported to a MIDI file format. There isu a lot of music theory involved in this library, so I recommend that you understand at least some of it before using it. If you have a good understanding of music theory, you should be able to use it quickly after reading the tutorials I have written.

Special reminder: In musicpy, except some music theory functions, the indexing of the music theory types starts from 0 (0-based), such as chord type, scale type, piece type, etc.

In musicpy, the most basic data structures are note, chord and scale. These classes are the basis of music code. musicpy has a lot of music theory functions, so let's start with the most basic ones.

First of all, we need to declare that all note lengths and note intervals in musicpy are in 4/4 time signature, which can be integers, floats or fractions. The tempo is in BPM, which is the number of beats you can play in 1 minute. In 4/4 time signature, 1 bar is 4 beats, 1 beat is 1/4 bar, that is, the number of bars played per minute is BPM/4, the time length of 1 bar in seconds is 240/BPM. All bars in musicpy are treated as 4/4 time signature.

In this chapter, we will introduce some of the most important and most commonly used data structures of musicpy.

## note

Initializing an instance of note just gives you a note name (such as C, Eb, A#, could also be lowercase) and an octave number (an integer), and now you can use that note to do anything in the music. You can also set the duration and volume of the note. The note length defaults to 0.25 (1/4 bar) and the volume defaults to 100.

For example. 

```python
a = note('A', 5)
```

This assigns the note A5 to a, which is represented as follows.

```python
A5
```

represents the note name and the octave number, which together determine the pitch.

When you use `note` to construct note types, the octave number could be omitted, the default value is 4.



### The composition of note type

```python
note(name,
     num=4,
     duration=0.25,
     volume=100,
     channel=None)
```

- name: the name of the note (C, D, E, G#, Gb, ...) , a string representing the name of the note

- num: the octave number, which is an integer, it determines the pitch of a note together with the note name

- duration: the length of the note in bars, e.g. duration = 1 means that the note is 1 bar long, the default value is 0.25

- volume: the intensity of the note, corresponding to the intensity of the note in the MIDI file, ranging from 0 to 127, with a default value of 100

- channel: the MIDI channel number of the note, when write to MIDI file, if channel is not None, then it will write to the corresponding channel

- degree: the pitch number of a note, C0 is 12, each octave has 12 notes, for example, the pitch number of C1 is 24, the pitch number of D1 is 26, the pitch number of C5 is 72, and so on, each note will automatically calculate its own pitch number corresponding to its name and octave number and store it, which is very useful afterwards. (The pitch number is the MIDI number that corresponds to the note in the common standard for MIDI files)

Because of this basic property of pitch number, the note class itself is equivalent to a pure number, i.e. it can be used as a pure number, and the chord class is a collection of note classes. It also means that the chord class itself is equivalent to a set of all numbers, and can be treated as a vector or even a matrix (For example, the concatenation of multiple chords can be seen as a concatenation of vectors, and therefore as a matrix). Therefore, the data structures of this language are designed in such a way that notes, chords, and scales can be used for mathematical operations. For example, operations in the field of linear algebra, operations in the field of discrete mathematics, and so on. It is also possible to build a set of algorithms for musical logic based on the data structure of the language. It is possible to combine pure mathematical logic to perform various aspects of musical analysis. Many experiments in the field of modern music, such as sequentialism, incidental music, and postmodernism (e.g., minimalist music), have been developed. Post-modernist music (e.g., minimalist music) can all theoretically be created rigorously on the basis of the purely digital data structures of this language. Even without mentioning experimental music, the language can be used to write any classical, jazz, or pop music.



## chord

This should be the most important class. In musicpy, a chord class is defined as "a set of notes", which is perhaps more general than the definition of a chord in music theory, because a complete piece of music can fit into a chord class, and it does in this library.

You can use the chord type to represent a chord, and also a melody, or the combination of both.

To initialize a chord instance, you just need to give a list of notes. You can also set the duration (the length of all notes), the interval (the interval between notes, expressed as a list). One of the more user-friendly things here is that you don't need to initialize the note list with the note class first. Instead, you can just write the names of the notes (strings).

For example:

```python
Cmaj7 = chord(['C5', 'E5', 'G5', 'B5'])
```

This writes a C major seventh chord.

(There are many more ways of constructing chord types, which could be written more concisely than here, you can refer to the basic syntax chapters for details)

We can play this chord with the play function:

```python
play(Cmaj7)
```

This C major seventh chord is represented as follows.

```python
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0)
```

If you want to create a melody in musicpy, the logic is the same as creating a chord, here is an example

```python
melody = chord('C5, C5, G5, G5, A5, A5, G5, F5, F5, E5, E5, D5, D5, C5',
                duration=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4],
                interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4])
```

You can play this melody, for example, at 80 BPM

```python
play(melody, bpm=80)
```

### The composition of chord type

```python
chord(notes,
      duration=None,
      interval=None,
      rootpitch=4,
      other_messages=[],
      start_time=None,
      default_duration=1 / 4,
      default_interval=0,
      default_volume=100)
```

- notes: a list of all the notes of the chord (or piece)

- duration: The length of each note of the chord, the default value is None, or the length of the note itself if it is None, or the length of the note if it is an integer, a float or a list

- interval: The interval between each two consecutive notes, in bars, as a list of note intervals (if initialized as an integer or a float, set all intervals to this integer or float) The default value is None, if the interval is not specified, all of the intervals of notes are 0 by default. **Please note, the definition of the interval of notes here is the interval from the beginning of current note to the beginning of the next note.**
  
- rootpitch: If the element of the note list is not a note type, but a string representing a note, it will be converted to a note type using the to_note function. If the note string does not have an octave, but only the name of the note, the rootpitch will be used as the octave of the note, with a default value of 4

- start_time: The start time of the chord type in bars, you can understand it as the rest from the beginning to the beginning of the first note, the default value is 0

- default_duration: the default duration for each note

- default_interval: the default interval for each note

- default_volume: the default volume for each note



## scale

This class can represent a specific scale. Using this class you can quickly build a scale according to the interval of the notes, for example, the arrangement of the major notes is whole whole half whole whole whole half (whole for whole step, half for half step), so if you want to build a C major scale, you can write

```python
scale('C5', interval=[2, 2, 1, 2, 2, 2, 2, 1], name='major')
```

This gives us the C major scale with C5 as the root note, expressed as follows

```python
[scale]
scale name: C5 major scale
scale intervals: [2, 2, 1, 2, 2, 2, 1]
scale notes: [C5, D5, E5, F5, G5, A5, B5, C6]
```

Of course, for most of the well-known scales, you only need to enter the name of the scale. For example

```python
scale('C5', 'major')
```

and you get the C major scale with C5 as the root note.

```python
[scale]
scale name: C5 major scale
scale intervals: [2, 2, 1, 2, 2, 2, 2, 1]
scale notes: [C5, D5, E5, F5, G5, A5, B5, C6]
```

For example

```python
scale('C5', 'minor')
```

Get the C minor scale with C5 as the root note.

```python
[scale]
scale name: C5 minor scale
scale intervals: [2, 1, 2, 2, 2, 1, 2, 2]
scale notes: [C5, D5, D#5, F5, G5, G#5, A#5, C6]
```

etc.
The scaleTypes in database.py are all musicpy's own scales, but users can also customize their own scales.



### The composition of scale type

```python
scale(start=None,
      mode=None,
      interval=None,
      notes=None)
```

- start: The main note of the scale (start note), which is a note class

- mode: The name of the scale, such as major, minor, dorian, lydian, etc.

- interval: The interval of a scale, 1 for a seminote, 2 for a whole note, 3 for an increasing second, and so on, in the form of a list, e.g. the interval of a major scale is [2,2,1,2,2,2,1].

- notes: The list of notes, see the list of notes in the chord class, a scale itself is a definite set of notes, so notes is all the notes in a scale instance, could also be a chord instance

The built-in methods of the scale class are rich in musical logic functions, such as harmonic functions, tonic chord, dominant chord, subdominant chord, secondary dominant chord of a degree, and so on. Extraction of natural triads and natural seventh chords from the scale in a certain number of steps, modulation in a circle of fifths in a certain number of steps in clockwise or counterclockwise direction, relative key, parallel key, negative harmony (mirror harmony), chord progression extraction by step, modulation to a specified key, derivation of the key from a degree of the note and get the standardized note name notation (the sharp and flat notation of the note names in each key), etc. I will explain the details in the section on basic syntax and how to use it.



## piece

When we need to write a piece with multiple tracks and each track with its own instrument, we could use the piece type. An instance of the piece type can store any number of tracks, and each track can have its own instrument, and the instrument can be changed at any time via MIDI messages.

There are detailed introductions of piece type in `Basic syntax of piece type`.



## track

The track type is a data structure used to store information about a single track in a piece type. Although the piece type itself does not consist of track types, the track type can be extracted from or added to the piece type, and the track type itself can be played and written to MIDI files directly.

There are detailed introductions of track type in `Basic syntax of track type`.



## drum

The drum type is a special data structure dedicated to representing drum beats, also known as percussion rhythms. The drum type is essentially very similar to the chord type, which also internally stores note types that can correspond to different types of drum beats on the drum track when written to a MIDI file. The most important feature of the drum type is that it can be built using a unique syntax for writing drums. This syntax is relatively simple, does not require consideration of which note corresponds to which type of drum beat in the MIDI file, and supports a certain degree of batch processing.

There are detailed introductions of drum type in `Basic syntax of drum type`.



## tempo

The tempo type can be used to change the tempo (BPM) of the current piece in real time. Instances of the tempo type must be placed in the `tempos` list of the chord type, setting the time in bars at which the change begins. The tempo type can act on chord types, piece types and track types, and is also stored as a MIDI event in the MIDI file after it has been written to it.

There are detailed introductions of tempo type in `Basic syntax of tempo type`.



## pitch_bend

The pitch_bend type can be used to change the pitch of the notes of a segment in real time, which can be very subtle. Instances of the velocity type must be placed in the `pitch_bends` list of the chord type, setting the time in bars at which the change begins. pitch_bend types can act on chord types, piece types and track types, and is also stored as a MIDI event in the MIDI file after it has been written to it.

There are detailed introductions of pitch_bend type in `Basic syntax of pitch_bend type`.



## pan

The pan type is a type specifically used to store the position of the left and right channel mixing. Using the pan types in the piece type allows you to set the pan of each track.

There are detailed introductions of pan type in `Basic syntax of pan type`.



## volume

The volume type is a type dedicated to storing the overall volume level of a track. Using the volume type in the piece type allows you to set the overall volume level of each track.

There are detailed introductions of volume type in `Basic syntax of volume type`.



## rest

Currently, the definition of a rest in musicpy is a data structure that can be passed in during chord type construction and merging, but does not exist as a note in the note list of the chord type, because the interval between adjacent notes is already defined by the list of note intervals of the chord type, so there is not much need for rests to exist in the chord type at this time. When you pass in rests when building a chord type, the rests are reflected in the list of note intervals, but the rests themselves are not added to the note list of the chord type. Currently the note list of chord types can contain only three data structures: note type, tempo type, and pitch_bend type.



### The composition of rest type

```python
rest(duration=1/4, dotted=None)
```

- duration: The duration of the rest in bars
- dotted: The number of dotted notes of the rest, the default value is None, which is not a dotted note



### Use rest when constructing chord types

```python
# add a half rest between the note D and E
C1 = chord(['C', 'D', rest(1/2), 'E'])

>>> C1
chord(notes=[C4, D4, E4], interval=[0, 1/2, 0], start_time=0)
```



### Use rest when merging chord types

```python
C1 = C('Cmaj7')
C2 = C('Dmaj7')
C3 = C1 | rest(1/2) | C2

# or using a number
# C3 = C1 | 1/2 | C2

>>> C3
chord(notes=[C4, E4, G4, B4, D4, F#4, A4, C#5], interval=[0, 0, 0, 3/4, 0, 0, 0, 0], start_time=0)
```



## beat

This is a data structure that represents meter in music theory, which is used in a rhythm.

A beat instance holds a single beat with a duration and a dotted number (in case it is a dotted beat).

You can form a complete rhythm with a list of beat instances.



### The composition of beat type

```python
beat(duration=1/4,
     dotted=None)
```

* duration: the duration of the beat in bars (without the dotted number)
* dotted: the dotted number of the beat, if it is None, the beat is not a dotted beat

You can use the `get_duration` method of the beat instance to get the actual duration of the beat by applying the dotted number, this method also applies to rest_symbol and continue_symbol.



## rest_symbol

This is a data structure that represents a rest in music theory, which could be used along with the beat type to form a rhythm.

The rest_symbol instances take the same parameters as the beat instances.

In practice, you can use `rest` instances interchangeably with `rest_symbol` instances, but it is recommended to use `rest_symbol` instances to form a rhythm, because there is a `continue_symbol` type that works together with it, it is better that their names are more standard.

```python
rest_symbol(duration=1/4,
            dotted=None)
```



## continue_symbol

This is a data structure that extends the previous note's duration and interval, which could be used along with the beat type to form a rhythm.

The continue_symbol instances take the same parameters as the beat instances.

```python
continue_symbol(duration=1/4,
                dotted=None)
```



## rhythm

This is a data structure that represents a rhythm, which is equivalent to a list of beats, rest symbols and continue symbols.

A rhythm instance can be applied to a chord instance to change the intervals and durations of a chord instance.

You can think of this data structure as a higher level abstraction of the drum type.

There are detailed introductions of rhythm type in `Basic syntax of rhythm type`.



## Interval

This is a data structure that represents a pitch interval, such as major third, perfect fifth in music theory.

These pitch intervals are stored in `database` module, each pitch interval has several ways to retrieve, such as abbreviation like `P5, M3, m7` (perefect fifth, major third, minor seventh), or full name like `perfect_fifth, major_third, minor_seventh`.

You can add or subtract pitch interval from a note or a chord, which will raise or lower the note or chord by the given pitch interval, for example:

```python
note1 = N('C4')

>>> note1 + database.m3
Eb4

>> note1 - database.m3
A3

chord1 = C('Cmaj7', pitch=4)

>>> chord1 + database.m3
chord(notes=[Eb4, G4, Bb4, D5], interval=[0, 0, 0, 0], start_time=0)

>>> chord1 - database.m3
chord(notes=[A3, C#4, E4, G#4], interval=[0, 0, 0, 0], start_time=0)
```

### The composition of Interval type

```python
Interval(number, quality, name=None, direction=1)
```

* number: the interval number, should be an integer between 1 and 17
* quality: the interval quality, should be one of` ['P', 'M', 'm', 'd', 'A', 'dd', 'AA'] ` or multiples of each
* name: the name of the pitch interval
* direction: the direction of the pitch interval, set to 1 to be positive, -1 to be negative

You can initialize a pitch interval instance like this:

```python
interval1 = database.Interval(number=3, quality='M')
>>> interval1
M3
```


## chord_type

This is a data structure that represents how a chord is derived in details, include the root note, chord type, inversions, omissions, alternations, chord voicings, compound chords and so on. This data structure is currently used mainly in the chord analysis functions in algorithm module, which helps to store the informations and procedures of how a set of notes turn into a chord in the desired order.

### The composition of chord_type type

```python
root: str = None
chord_type: str = None
chord_speciality: str = 'root position'
inversion: int = None
omit: list = None
altered: list = None
non_chord_bass_note: str = None
voicing: list = None
type: str = 'chord'
note_name: str = None
interval_name: str = None
polychords: list = None
order: list = None
```

* root: the root note of the chord

* chord_type: the chord type of the chord, such as `maj7`, `maj9`

* chord_speciality: the speciality of the chord, could be one of `root position`, `inverted chord`, `altered chord`, `chord voicings`, `polychord`

* inversion: the inversion number of the chord if it is a inverted chord

* omit: the omitted notes of the chord

* altered: the altered notes of the chord

* non_chord_bass_note: the non-chord bass note of the chord

* voicing: the voicing of the chord

* type: the type to differentiate a single note, pitch interval and chord

* note_name: the note name if type is a single note

* interval_name: the interval name if type is a pitch interval

* polychords: the list of chord_type instances if it is a polychord

* order: a list of integers that represents the derivation order of the chord, the meanings of the integers are:

  ```
  0: omit some notes
  1: alter some notes
  2: inversion
  3: chord voicing
  4: add a non-chord bass note
  ```


Use `to_text` method of a chord_type instance to get the full chord name, `to_chord` method to get the chord derived from the stored information, `get_root_position` to get the root position chord name.

# Basic syntax of note type

## Construct a note using its name and octave number

```python
a = note('D', 6)
```

a is the note D6.
Other parameters of note are duration (note length in bars), volume (note strength, corresponding to MIDI 0~127, i.e. any integer between 0 and 127 (including 0 and 127)), channel (MIDI channel number)
For example

```python
a = note(name='C', num=5, duration=0.5, volume=100)
```

means that a is note C5, the note length is 0.5 bars, and the note strength is 100.



## Construct a note by entering the note name directly (note name + number of octaves)

We can use the to_note function

```python
to_note('E5')
```

The note E5 is obtained.

A shortened version of the to_note function would be

```python
N('E5')
```

N is the initial capitalization of the note note



## Set the note length and volume for existing notes

```python
a.set(duration, volume) # Returns a new chord type
a % (duration, volume) # Advanced syntax
a = a % (duration, volume) # Write it this way if you want to replace the original note type directly, or just use it alone
```

duration is the note length in bars, volume is the note strength, corresponding to MIDI 0~127, any integer between 0 and 127 (including 0 and 127)

You can set only one of these parameters, (you can leave it blank if you don't set it) or you can set both of them. Using the built-in function set for note types returns a new note type with modified parameters. It is completely independent from the previous note type, because when writing musicpy code, you can build blocks to write parameters such as pitch, note interval, note duration, volume level, etc. in one sentence. This is also one of my requirements for the syntax design of musicpy. The set methods for other music types such as chord types are similar to this, I will explain this in more detail when I talk about chord types.



## Converting pitch numbers of notes to note types and getting pitch numbers from note types

You can convert an integer to a note using the degree_to_note function, for example

```python
degree_to_note(60)
```

get a note type C4.


To get the number of pitches of a note type a, you just need

```python
a.degree
```

and that's it



## To raise or lower a note

```python
a.up(n)
```

Raises the a note by n semitones

```python
a.down(n)
```

means lower the a note by n semitones

Advanced syntax:

```python
+++a #(note a raised by 3 semitones)
---a #(note a lowered three semitones)
a + n #(note a raised by n semitones)
a - n #(note a lowered by n semitones)
```

(analogous to the rising and falling notes of the chord class)



## The sharp and flat signs of notes are converted into each other

For example, if the note a has the note name C#, then

```python
~a
```

gets the flat representation of the note a

```python
Db
```

For example, if the note b has the sound name Eb, then

```python
~b
```

gets the sharp representation of the note b

```python
D#
```



## Combining multiple notes to form a chord

For example, if you have four notes a, b, c, and d, you can join them with a + sign to form a chord with the notes a, b, c, and d in that order.

```python
A = a + b + c + d
```

The chord A is composed of the notes a, b, c, d



## Note types have a new music theory function that allows you to add chord names to get chord types

Note types can be passed in as functions or generators to get chord types, e.g.

```python
A3 = N('A3')
>>> print(A3('sus'))
chord(notes=[A3, D4, E4], interval=[0, 0, 0], start_time=0)
# Also supports inversion, polychords, and other C functions that support the syntax of parsed chord names
```



## Note type adds the function of generating chords according to the interval relationship

You can use the `with_interval` function of the note type to specify an interval to form a chord type with two notes. The two notes are the current note type and the note type that forms the specified interval relationship with this note type.

```python
a = N('C5')
>>> a.with_interval(database.major_seventh) # form a chord representing the major seventh interval of C5
chord(notes=[C5, B5], interval=[0, 0], start_time=0)
```



## Usage of dotted notes

There are several ways you can use dotted notes. First, note types can use the `dotted` function to change the length of a note to the length of a dotted note, allowing you to customize the number of dots attached. Chord types can also use the `dotted` function to change a note, some notes or all notes in a chord type to dotted notes, and you can also customize the number of dots.

In addition, when using the advanced syntax and translate functions to construct chord types and drum types, you can also use dotted notes, with the syntax of adding `. `, you can add as many dots as you want, and the length and spacing of the notes will be calculated based on the number of dots you add.

```python
a = N('C5')

>>> a.duration
0.25

b = a.dotted() # Get the dotted notes of note type a (single dotted)

>>> b.duration
0.375

c = a.dotted(2) # Get the dotted notes of note type a (double dotted)

>>> c.duration
0.4375

# The dotted function for the chord type
dotted(ind=-1, num=1, duration=True, interval=False)

# ind: index of the note that becomes dotted, can be an integer index, starting from 0
# or 'all', which means all notes become dotted, or a list of indices, starting from 0, default is -1

# num: the number of dots, the default is 1

# duration: whether to change the length of the note to a dotted note, default is True

# interval: whether to change the note interval to the length of the dotted notes, the default value is False

a = C('C')

>>> a.get_duration()
[0.25, 0.25, 0.25]

b = a.dotted() # change the last note of chord type a to dotted (single dotted)

>>> b.get_duration()
[0.25, 0.25, 0.375]

c = a.dotted([0, 2]) # turns the 1st and 3rd notes of chord type a into dotted notes (single dotted)

>>> c.get_duration()
[0.375, 0.25, 0.375]

a = chord('C5[.8.;.] , D5[.8;.] , E5[.8.;.] , F5[.8;.]')
# The first and third notes are dotted eighth notes, the second and fourth notes are normal eighth notes

a = translate('C5[.8.;.] , D5[.8;.] , E5[.8.;.] , F5[.8;.]') # Same as above, using the translate function
```



## Reset note pitch

You can use `reset_pitch` function of the note type to reset the note name of a note type, while the octave remains unchanged, `reset_octave` function to reset the octave of a note type, while the note name remains unchanged, `reset_name` function to reset the note name along with the octave by a note name string like `C5`. All of these functions return a new note instance with the new note pitch, while other attributes remain unchanged.

```python
a = N('C5', duration=2)

b = a.reset_name('A5')

>>> b
A5

>>> b.duration
2

c = a.reset_pitch('E')

>>> c
E5

d = a.reset_octave(3)

>>> d
C3
```



## Comparing two notes

When comparing two notes, if the two notes are equal, it means that the two notes correspond to the same pitch in twelve equal temperament, independent of the note name and other attributes. If one note is smaller than the other, it means that it has a lower pitch than the other note.

```python
a = N('C#5')
b = N('Db5')

>>> a == b
True

a = N('C5')
b = N('c5')

>>> a == b
True

a = N('C5')
b = N('D3')

>>> a == b
False

>>> a > b
True
```

# Basic syntax of a drum type

Added in early May 2021, the drum type is a new music theory type that reads a string that follows a specific syntax rule and converts it to a drum beat.

I have designed a new syntax for writing drum beats, and have successfully written an interpreter function that can parse strings that conform to this syntax into a MIDI file of drum notes. I'll explain this syntax for drum beats in code.

First of all, you can define your own dictionary of numbers or letters or special characters to map to different MIDI drum notes, I have defined a default drum mapping dictionary in the database.

Note that here the string that maps to value -1 (`0` as default) will be interpreted as rest symbol, which adds extra interval to the previous note, the string that maps to value -2 (`-` as default) will be interpreted as continue symbol, which adds interval and extend the duration of the previous note.

Here the length of numbers, letters and special characters can be greater than 1, which means you can write multiple digits, words and multiple special characters as a whole for mapping.

This is the current default drum mapping dictionary, there are two sets of templates you can choose to use, or you can customize the drum mapping dictionary.

```python
drum_mapping = {
    'K': 36, # Electric Bass Drum
    'H': 42, # Closed Hi-hat
    'S': 40, # Electric Snare
    'S2': 38, # Acoustic Snare
    'OH': 46, # Open Hi-hat
    'PH': 44, # Pedal Hi-hat
    'HC': 39, # Hand Clap
    'K2': 35, # Acoustic Bass Drum
    'C': 57, # Crash Cymbal 2
    'C2': 49, # Crash Cymbal 1
    '0': -1, # rest
    '-': -2 # the continuation of last note
}

drum_mapping2 = {
    '0': 36,
    '1': 42,
    '2': 40,
    '3': 38,
    '4': 46,
    '5': 44,
    '6': 39,
    '7': 35,
    '8': 57,
    '9': 49,
    'x': -1,
    '-': -2
}
```

Here the different strings of numbers map to values that are MIDI drum notes. The different values represent different pitches, and in the case of drums represent different kinds of drums. Now we can write a music theory type drum, whose 1st argument is a string, and in this string you can write drums according to the drum syntax I designed, which can represent complex drums relatively concisely.  

Single drum beats, spaced by `,`, indicate sequential playing (e.g. big drum, hihat, snare drum, hihat, big drum, hihat, snare drum, hihat).

```python
'K, H, S, H, K, H, S, H'  
```

Multiple different drum beats played at the same time, spaced by `;`, indicating simultaneous playing. The drum beats combined in this way could be called `note group`.

```python
'K, K;H, S, H, K, K;H;PH H;S, H'
```

If there is an interval between two drums (drums can be monophonic or polyphonic), it is expressed in the form `i:n`, with n indicating the interval and n being any integer, decimal or fraction in bars.

```python
'K, i:1, S, H, i:1, K, S, H'
```

Each drum beat can be followed by a settings block, also including drum beats played at the same time (drums concatenated with `;`). The settings block only apply to the note or note group it attaches.

```python
'K[l:1/4]'
```

In the settings block, if there are parameters you don't want to set, you can write `n` to indicate that you don't want to set them, and use them to set to the batch setting statement if there is one later. Please note that the batch setting statement will overwrite the setting of each drum block, unless `n` is written to indicate no setting.

```python
'K[l:1/4;i:n;v:80]'
```

Note that if drums that are played simultaneously (drums that are joined with ;) are set for the settings block, put it after the last note.

```python
'H;S[l:1/4;i:1/8]'
```

Keyword headers can perform a variety of different functions on the drums within their range of action. The drums are segmented by keyword headers or bar lines `|`, and each keyword headers acts on the drums between the previous keyword headers or bar lines and it. For example, `K, H, S, H, r:2`, here `r:2` repeats the previous part twice.

Some of the keyword header can be placed in the settings block, separated by `;`.

Here is a description of the function of each keyword header:

| Keyword  | Functionality at outside                                     | Functionality in settings block                              |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| r:n      | repeat the drum beats n times                                | repeat the drum beats n times, lengths and intervals of each note in the settings block are divided equally according to the number of repetitions when there is a fixed length assigned to it |
| R:n      |                                                              | repeats the drum beats n times, and when there is a fixed length assigned to it, the lengths and intervals of each note is not divided equally |
| d:l;i;v  | set the default length l, interval i, volume v, or you can use dl, di, dv respectively |                                                              |
| a:l;i;v  | set all uniform lengths l, interval i, volume v, or use al, ai, av respectively |                                                              |
| t:n      | set the total length of the interval to n. The length of each note in the interval is the total length divided by the number of notes in the region, and can be occupied using empty notes (characters with a value of -1 in the drum mapping) and continuation notes (characters with a value of -2 in the drum mapping), for example `K, H, S, H, 0, K, S, H, K, -, S, H, K, K, S, H, t:2` This is a section where each note takes up 1/8 of a measure, the `0` is rest symbol, and the `- ` is the continuation of the previous note | same as outside                                              |
| b:n      | when the total length is set, set the number of beats in the region to n beats, this will assign a unit duration to each drum beat unit | if set in the settings block, set the duration to unit duration * n |
| B:n      |                                                              | works the same as the global case of b, valid when there is a set total length in the settings block |
| i:n      | insert interval of n bars in the middle of the note          | set the interval of the note to n bars                       |
| l:n      |                                                              | set the note length to n bars                                |
| v:n      |                                                              | set the note volume to n                                     |
| n:name   | set the name of the drum beat in the region                  |                                                              |
| u:name   | use the drum region with the name                            |                                                              |
| s:T      |                                                              | whether the note group are played simultaneously or not (T/F), if not, the drums will be divided equally by the length of one drum when the total length is fixed |
| cm:n     |                                                              | use for single continue symbol only, set the continue mode to n, the value could be 0 or 1, if value is 0, only extend the duration of the last note, if value is 1, when the previous note is a group, extend the duration of all notes in the group; if the continue mode is not set, the default action of continue symbol is extending only last note except when the previous note is a group that set to playing at the same time, which in case extending all notes in the group |
| cs:T     |                                                              | when you use chord types as a drum beat, whether the notes of chord are played simultaneously or not (T/F) |
| !keyword | Use ! in combination with the keyword header means to set all the current notes in batch, for example: K, H, S, H \| K, K, S, H, !r:2 |                                                              |

When there are no keywords specified in the settings block, the values are the same as the settings block when initializing a chord, which is `[duration;interval;volume]`.



## Caution

1. Please note that in the settings block, when the parameter is a list, you need to set a separate settings block, use `;` to separate the elements of the list, you can put multiple settings blocks together.
2. you can place any spaces and newlines, they will not affect the content after parser conversion, so you can write the drum code more beautiful and hierarchical.  
3. Note length and spacing can also be set using syntactic sugar, using `.n` for `1/n`, which is an nth note.



## Introduction to the construction and usage of drum types

Drum types are similar to chord types in that they have a list of notes and can be repeated n times, merged, set overall note parameters, etc. They can also be played directly, but please note that when you play a drum type using the play function (either using the built-in function of the drum type or using the global function), the drum type is automatically coded into a music type and sets the number of MIDI channels to 9 (counting from 0 as the first, i.e. the 10th channel of MIDI, dedicated to the drum track).  

Note that the drum type itself does not contain velocity, or tempo, or bpm, because the drum type is designed to be viewed on the same level as the chord type, and neither the drum type (drum) nor the chord type (chord) contains the velocity parameter.  

The drum type can be constructed by passing a string or a chord type, where the default position of the 1st parameter is a string, or can be specified with the pattern keywordword parameter, or with the notes keywordword parameter if you want to pass a chord type. If a string is passed in, the incoming string is parsed for drum syntax and converted to a chord type for storage in the drum type when the drum type is constructed. You can use the name keywordword argument to name the drums you write, and you can use the mapping keywordword argument to specify a dictionary of characters mapped to drum values, where drum values means the numbers corresponding to the different drums in general MIDI, and I have written which numbers correspond to the different drums in the drum_types in the database.  

You can use the `i` keywordword parameter to set the timbre of the drum kit, see the numbers corresponding to the timbre of the drum kit in general MIDI.  

Also, for chord types you can use the translate function, which uses the same set of syntax as writing drums to write chord types or a tune, just replace the custom characters with note names.



### The composition of drum type

```python
drum(pattern='',
     mapping=drum_mapping,
     name=None,
     notes=None,
     i=1,
     start_time=None,
     default_duration=1 / 8,
     default_interval=1 / 8,
     default_volume=100,
     translate_mode=0)
```

- pattern: the string to be parsed to drum beats
- mapping: the drum mapping dictionary, could be customized, the default value is drum_mapping
- name: the name of the drum beat
- notes: the chord type of the drum beat, could be passed in directly as drum beat, the default value is None, which is converting the pattern as drum beat
- i: the instrument type of the drum beat, corresponding to the instrument number of General MIDI
- start_time: the start time of the drum beat, if it is None, then use the start time of the chord type of the drum beat
- default_duration: default duration of drum beat
- default_interval: default interval of drum beat
- default_volume: default volume of drum beat
- translate_mode: set to 0 to translate as drum, set to 1 to translate as chord

```python
drum_example = drum('K, H, S, H, K;H, K;H, S, H, r:2')
# This is an example of a drum section with kick, hi-hat, snare, hi-hat at the beginning, then 2 simultaneous kick and hi-hat, then 1 single snare and 1 single hi-hat, and finally the whole section repeats 2 times,
# where K,H,S means kick, hi-hat and snare respectively, so K;H means kick and hi-hat playing at the same time
play(drum_example, 150) # Play the drums at 150bpm
>>> print(drum_example)
[drum] 
chord(notes=[C2, F#2, E2, F#2, C2, F#2, C2, F#2, E2, F#2, ...], interval=[1/8, 1/8, 1/8, 1/8, 0, 1/8, 0, 1/8, 1/8, 1/8, ...], start_time=0)

# If you use drum type as track in a piece type, you must use the notes attribute of the drum type as chord type,
# and set the corresponding channel number to 9
piano1 = C('Cmaj7') % (1, 1/8)
piece_example = P([piano1, drum_example.notes], [1, 1], channels=[0, 9])
play(piece_example)
```

# Basic syntax of a chord type

## Setting the interval and duration of a chord

For example, if you have a chord A and you want to set the note interval to 1 bar and the note duration to 1.5 bars, you can use the built-in method set of the chord class. The first parameter of set is the note duration duration, and the second parameter is the note interval interval.

```python
A.set(1.5, 1)
```

The result is a new chord type with all the note durations of chord A set to 1.5 and all the note intervals set to 1. Note that instead of modifying the internal properties of chord A, a new chord is returned with the modified internal properties of chord A. If you have different settings for note duration or note interval for each note, you can pass in a list, for example

```python
A.set([0.5, 0.5, 1, 1], [1, 1, 2, 2])
```

Returns a chord with note durations of 0.5, 0.5, 1, 1 (in bars) and note intervals of 1, 1, 2, 2 (in bars).

Advanced syntax:

```python
A % (1.5, 1)
```



## Get a chord based on its root note and chord name

Introducing a very handy function: get_chord. This function allows you to get the type of chord you want, simply by giving the root note of the chord and the chord type. e.g.

```python
Am7 = get_chord('A', 'm7')
```

This way we create a minor seventh chord of A. It is represented as

```python
chord(notes=[A5, C6, E6, G6], interval=[0, 0, 0, 0], start_time=0)
```

There are many types of chord types, which can be found in the chordTypes file in database.py. You can also add your own chord types by writing the chord name and the corresponding chord interval in the same format as in chordTypes.
The first parameter of the get_chord function is the root note of the chord, and if no specific pitch is specified (e.g. C5, D6 is a note with a specific pitch), then by default it is treated as the 4th octave, e.g. get_chord('A', 'm7'), which is equivalent to
get_chord('A4', 'm7'), and if you specify a specific pitch for the root note, for example, if you now want to write a major 7th chord with root note D6, you can write:

```python
Dmaj7 = get_chord('D6', 'maj7')
```

In addition, the get_chord function has a very large number of parameters that can be used to set the chord's omission, altered notes, added notes, as well as the exact duration of each note of the chord, the interval of the notes, etc. You can even enter the intervals of the notes to build the chords (you can also set the value of cumulative to determine whether you want to enter the interval of each note to the root note or the interval between each two notes). In musicpy, the name of each interval is already defined and can be used directly, for example, the value of major_third is 4, which is the number of semitones in the major third. For example, to construct a C major seventh chord according to the intervals, you can write it like this

```python
get_chord('C5', interval=[database.major_third, database.perfect_fifth, database.major_seventh])
```

The result is

```python
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0)
```

When a chord has an interval of all 0s, the chord is all notes together at the same time. If an interval is 0, it means that two notes start playing together at the same time.



## Constructing chords from note names, note durations and note intervals

For example, if we want to build a major seventh chord with a root note of C5, a note interval of one bar between each note, and a note duration of two bars, then we can write it like this

```python
chord(['C5', 'E5', 'G5', 'B5'], interval=1, duration=2)
```

If the note interval and note duration are not the same, then you can pass a list in, e.g.

```python
chord(['C5', 'E5', 'G5', 'B5'], interval=[0.5, 0.5, 0, 2], duration=[1, 2, 0.5, 1])
```

In addition to the list of strings, you can also write all the notes in one string, for example, now we want a C major seventh chord with C5 as the root note, so we can write

```python
chord('C5, E5, G5, B5')
```

or

```python
chord('C, E, G, B', rootpitch=5)
```

The value of rootpitch defaults to 4, so if you want a C major seventh chord with C4 as the root note, you can just write

```python
chord('C, E, G, B')
```

The chord function takes a string with no pitch number at all, and normalizes the chord output according to the standardize function, which arranges the pitches of the notes in the string in the order of their names, and then forms the chord in the original position, for example

```python
chord('C, E, G, B, D')
```

will give you

```python
chord(notes=[C4, E4, G4, B4, D5], interval=[0, 0, 0, 0, 0], start_time=0)
```

Of course, it's most straightforward to receive a list of note types, like

```python
chord([N('C'), N('E'), N('G'), N('B'), N('D')])
```

However, if the chord function receives a list of note types or strings with a definite number of pitches, then no chord normalization is performed, because the pitch numbers of all notes are determined at this point. If you want to receive a string without chord normalization in the chord function, you can specify the pitch of the notes manually, for example

```python
chord(['C4', 'E4', 'G4', 'B4', 'D4'])
```

or

```python
chord('C4, E4, G4, B4, D4')
```

When using the chord function, when writing a string of note names or a list of string of note names, it is possible to write the note duration, note interval and volume in the string with a new syntax. For example, now we want to write a melody

```python
example = chord('G5, F5, E5, F5, E5, E5, D5, E5, D5, C5, B4, G4')
```

The list of note durations for this melody is

```python
example_duration = [3/4, 1/8, 1/8, 3/4, 1/8, 1/8, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2]
```

The list of note intervals for this melody is the same as the list of note durations

```python
example_interval = example_duration.copy()
```

If the traditional approach is

```python
example % (example_duration, example_interval)
```

With the new syntax it can be written as

```python
example = chord('G5[3/4;3/4], F5[.8;.8], E5[.8;.8], F5[3/4;.3/4], E5[.8;.8], D5[.8;.8], E5[.4;.4], D5[.4;.4], C5[.2;.2], B4[.2;.2], G4[.2;.2]')
>>> example
chord(notes=[G5, F5, E5, F5, E5, D5, E5, D5, C5, B4, ...], interval=[3/4, 1/8, 1/8, 4/3, 1/8, 1/8, 1/4, 1/4, 1/2, 1/2, ...], start_time=0)
```

Please note that the separator of the parameters inside the brackets must be `;`, the brackets should be square brackets, there can be spaces between parameters, the order of the parameters is [note duration; note interval; note volume], you can set only the note duration, or only the note duration and note interval, or all three parameters. The biggest advantage of this new syntax is that if you need to change the note duration of a note or the note interval between a note and the next note when writing a melody, you can change it directly after the note name instead of going to the note duration list and the note interval list to find the position of the note you want to change. The `chord` function also supports the list of note name strings with this new syntax.

note duration, note interval and volume can be integers, decimals or fractions. I also added a syntactic sugar here, if you want to enter notes like 2, 4, 8, 16, then you can write `.n` for n notes, which is equivalent to 1/n of the note duration. If the note duration is, for example, 3/4, then you can just write 3/4.

In addition, the new syntax of the chord function has a unique syntactic sugar, that is, when the note duration and note interval are the same, the note interval can be abbreviated as `. `. For example

```python
chord('G5[3/4;.] , F5[.8;.] , E5[.8;.]')
```

To insert rests, you can use syntax like `r[duration]` as notes in the string, the nth note syntactic sugar is also accepted, the unit of the duration of rests is bar, the continuation symbol `-` is also supported to extend the length and interval of the previous note, for example

```python
example = chord('G5[3/4;3/4], F5[.8;.8], E5[.8;.8], F5[3/4;1/4], r[.2], E5[.8;.8], D5[.8;.8], E5[.4;.4], D5[.4;.4], C5[.2;.2], B4[.2;.2], G4[.2;.2]')
>>> example
chord(notes=[G5, F5, E5, F5, E5, D5, E5, D5, C5, B4, ...], interval=[3/4, 1/8, 1/8, 3/4, 1/8, 1/8, 1/4, 1/4, 1/2, 1/2, ...], start_time=0)
```

If you want multiple notes to be played at the same time, you can use `;` to join multiple notes together, for example `C5;E5;G5`.

Sometimes relative pitch can be more convenient when constructing chords without considering absolute pitch, so the syntax of relative semitones is also supported. The syntax is as follows:

* Use `+n` to indicate that the previous note is raised by n semitones, but the reference note used to calculate the relative pitch does not change
* Use `++n` to indicate that the previous note is raised by n semitones and the reference note used to calculate the relative pitch becomes the current note
* Use `+no` to indicate that the previous note is raised by n octaves, and `+nom` to indicate that the previous note is raised by m semitones and then being raised by n octaves, which also supports the `++` syntax
* Change the above syntax to `-` to lower pitch
* Syntax using relative pitch must be preceded by at least one absolute pitch

Here are some examples:

```python
example = chord('A#4, +7, +10, +1o2, +1o3, +1o5, +1o3, +1o2', default_interval=1/8, default_duration=1/8)
>> example
chord(notes=[A#4, F5, G#5, C6, C#6, D#6, C#6, C6], interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8], start_time=0)

example2 = chord('C5, ++2, ++2, ++1, ++2', default_interval=1/8, default_duration=1/8)
>> example2
chord(notes=[C5, D5, E5, F5, G5], interval=[1/8, 1/8, 1/8, 1/8, 1/8], start_time=0)
```



## Get a chord based on chord name

The trans function can be used to parse the full chord name and return the corresponding chord. It supports root position chord representation, inverted chord representation, polychord representation, etc.
The first parameter of the trans function is the chord name, the second parameter is the pitch of the root note of the chord (the default value is 4), and the third parameter is the duration (the duration of the note, default is 0.25), and the fourth parameter is interval (the interval of the note, default is None, the returned chord interval is 0), or you can write `note:chord_type` to indicate the specific note octave.
For example:

Dmaj7 chord and Dmaj7 chord with D5 as the root note

```python
>>> trans('Dmaj7')
chord(notes=[D4, F#4, A4, C#5], interval=[0, 0, 0, 0], start_time=0)

>>> trans('D5:maj7')
chord(notes=[D5, F#5, A5, C#6], interval=[0, 0, 0, 0], start_time=0)
```

the second inversion of the F major triad

```python
>>> trans('F/C')
chord(notes=[C5, F5, A5], interval=[0, 0, 0], start_time=0)
```

The inversion parsing can also take numbers, for example:

the first inversion of the C major triad E, G, C

```python
trans('C/1')
```

the C major triad by putting the 1st note to the highest note of the chords E, G, C

```python
trans('C/-1')
```

the inversion E, C, G for a C major triad that puts the second note to the lowest note (as opposed to the traditional inversion)

```python
trans('C/1!')
```

C major triad

```python
>>> trans('C')
chord(notes=[C4, E4, G4], interval=[0, 0, 0], start_time=0)
```

polychord with the A minor triad over the G minor triad

```python
>>> trans('Am/Gm')
chord(notes=[G4, A#4, D5, A5, C6, E6], interval=[0, 0, 0, 0, 0, 0], start_time=0)
```

G major triad plus a C chord on the lowest note

```python
>>> trans('G/C', 6, 1, 1)
chord(notes=[C6, G6, B6, D7], interval=[1, 1, 1, 1], start_time=0)
```

The syntax of add and sus, by entering `addN` you can add a certain number of degrees from the lowest note, and by entering `susN` you can get the previous chord type sus2 or sus4 chords.

```python
>>> print(C('C,add9'))
chord(notes=[C4, E4, G4, D5], interval=[0, 0, 0, 0], start_time=0)

>>> print(C('Cm7,add11'))
chord(notes=[C4, D#4, G4, A#4, F5], interval=[0, 0, 0, 0, 0], start_time=0)

>>> print(C('Cmaj7,sus4'))
chord(notes=[C4, F4, G4, B4], interval=[0, 0, 0, 0], start_time=0)

>>> print(C('Bb9,sus'))
chord(notes=[Bb4, D#5, F5, G#5, C6], interval=[0, 0, 0, 0, 0], start_time=0)
```

A shortened way of writing the trans function:

```python
C(chord name, other arguments)
```

C is the initial capitalization of chord



## More advanced manipulation of a chord (alterations, omissions, polychords)

For example, if chord A is a C7 chord, then to get a C7#9 chord, you can write it like this

```python
A('#9')
```

The result is

```python
chord(notes=[C5, E5, G5, A#5, D#6], interval=[0, 0, 0, 0, 0], start_time=0)
```

The C7b9 chord is

```python
A('b9')
```

For example, if B is a Cmaj9 chord, then if you want to omit the third, you can write it like this

```python
B('omit3')
```

or

```python
B('no3')
```

Multiple altered and omitted notes can be separated by English commas, for example

```python
A('#5, b9, omit3')
```

If chord A is a C7 chord, then what you get is a C7#5b9 chord omitting a third.

To build a polychord, you only need to join two chords with '/', except in the case of two chords stacked on top of each other
There is also a polychord formed by adding a lowest note underneath a chord, in both cases a '/' is sufficient.
For example

```python
C('Amaj7') / 'D'
```

The result is

```python
chord(notes=[D4, A4, C#5, E5, G#5], interval=[0, 0, 0, 0, 0], start_time=0)
```

That is, the Amaj7 chord with D as the lowest note underneath.
The case of a polychord of two chords, e.g.

```python
C('A') / C('G')
```

yields

```python
chord(notes=[G4, B4, D5, A4, C#5, E5], interval=[0, 0, 0, 0, 0, 0], start_time=0)
```

This is a polychord of G major triad superimposed under A major triad.

In the chord name parsing structure, it is possible to enter and parse the advanced operations of the chord directly by simply separating them with commas, for example, the C major 7th chord omitting the 5th

```python
C('Cmaj7,no5')
```

The result is

```python
chord(notes=[C4, E4, B4], interval=[0, 0, 0], start_time=0)
```



## How to build an empty chord

If you want to build an empty chord with no notes, you can write

```python
chord([])
```

will give you

```python
chord(notes=[], interval=[], start_time=0)
```

An empty chord can be used as an initial chord for adding new chords in a loop, or as a chord type when treated as a piece (you can add new melodies or chord notes to it), for example

```python
chord([]) | C('Am') | C('F') | C('G')
```



## Generate chord types according to the interval relationship

You can use the `get_chord_by_interval` function to generate chord types from a list of interval relations. You can select the interval relationship with the root note or the interval relationship between every two adjacent notes.
The note type can also use this function, and the note type itself will be used as the starting note when used.

```python
get_chord_by_interval(start,
                     interval1,
                     duration=0.25,
                     interval=0,
                     cumulative=True)

# start: The starting note of the chord type, which can be a string representing a note or a note type
# interval1: Represents a list of interval relations, the elements are integers
# duration: the note duration of the generated chord type
# interval: The note interval of the generated chord type
# cumulative: If True, the interval relationship is the interval relationship with the initial note. If False, the interval relationship is the interval relationship between every two adjacent sounds. The default value is True

>>> get_chord_by_interval('C5', [database.major_third, database.perfect_fifth, database.major_seventh])
# Obtain the chord type composed of the initial note C5, and C5 in turn to form the major third, the complete fifth and the major seventh
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0) # Get the C major seventh chord

>>> get_chord_by_interval('C5', [database.major_third, database.minor_third, database.major_third], cumulative=False)
# Get the chord type composed of the initial note C5 and the adjacent intervals as the major third, minor third, and major third.
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0) # Get the C major seventh chord

a = N('C5')
>>> a.get_chord_by_interval([database.major_third, database.perfect_fifth, database.major_seventh]) #The note type calls this function
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0)
```



## Chord representation

In musicpy, a chord type is represented as

```python
# for example, a C major seventh chord with a root note of C5
>>> get_chord('C5', 'maj7')
chord(notes=[C4, E4, G4, B4], interval=[0, 0, 0, 0], start_time=0)
```



## Get the inversion of a chord

inversion gets the inversion of a chord, with a parameter num representing the inversion of the chord. For example.

```python
get_chord('A', 'm7').inversion(1) 
```

You can get the first inversion of the minor seventh chord of A, expressed as follows.

```python
chord(notes=[C6, E6, G6, A6], interval=[0, 0, 0, 0], start_time=0)
```

Advanced syntax: (I designed symbolic syntax for many functions of musicpy to write faster)

```python
get_chord('A', 'm7') / 1
```

The result is the same as get_chord('A', 'm7').inversion(1).
You can also write the note you want to invert after '/', and if the note is within a chord it will invert that note to the lowest note, e.g.

```python
get_chord('A', 'm7') / 'E'
```

The result obtained is

```python
chord(notes=[E6, G6, A6, C7], interval=[0, 0, 0, 0], start_time=0)
```

Which is the second inversion of the A minor seventh chord.



## Adding notes to a chord

If you want to add a note x to chord A, then just

```python
A + x
```

and that's it. What you get is a new chord with the note x added.



## Removing a note from a chord

If you want to remove a note x from a chord A, then you just need

```python
A - x
```

and that's it. What you get is a new chord with the note x removed.



## Repeating a chord a certain number of times

If you want to repeat a chord A n times, then you just need

```python
A * n
```

and that's it. What you get is a new chord repeated chord A n times.



## Arranging a chord in reverse order

If you want to arrange the notes inside a chord A in reverse order, then simply

```python
A.reverse()
```

and that's it. What you get is the new chord in reverse order.

Advanced syntax:

```python
~A
```

You can also get the chord A in reverse order.

```python
'''
Note that chord A here is not necessarily just a chord in music theory, but can be a melody, or even a melody with a chord underlay. This is because the definition of a chord class in musicpy is "a collection of notes". Therefore, an instance of a chord class in musicpy can store information about a whole piece. This information includes all the notes in the piece, the duration of each note, the velocity, and the interval between each two notes.
'''
```



## Get the interval relationship of a chord

The `intervalof` function returns the interval relationship between the notes of a chord. When the parameter `cumulative` is set to `True`, return the interval between each note and the root note, `False` to return the interval between every two adjacent notes. The default value is `True`, e.g.

```python
get_chord('C','maj').intervalof()
```

You will get `[4, 7]`, which means that there are four semitones between the second note and the root note inside the C major triad (C,E,G) (major third), and seven semitones between the third note and the root note (perfect fifth). If you want to see the names of the intervals in music theory, then you can set the parameter `translate` to `True`, then you can see the names of the corresponding intervals. For example.

```python
get_chord('C','maj').intervalof(translate=True)
```

will get `[M3, P5]`, which means major third and perfect fifth.

When `cumulative` is set to `False`, returns the interval between every two notes of the chord from low to high, e.g.

```python
get_chord('C','maj').intervalof(translate=True, cumulative=False)
```

will get `[M3, m3]`, which means that a C major triad is composed of a major third and a minor third.



## Indexing a chord, slicing (by indexing worth to a certain note of a chord, or a fragment of a range)

For example, now we have a chord A.

```python
A = get_chord('C', 'maj7')
```

If we want to get the 1st note of the chord A, then we write

```python
A[0]
```

If we want to get the 2nd note of the chord A, then write:

```python
A[1]
```

If we want to get the last note of chord A, then write:

```python
A[-1]
# Note that the index value of the chord starts from 0 as the first note, that is, 0 corresponds to the first note of the chord, 1 corresponds to the second note of the chord, and so on.
# To get the penultimate first note of the chord, the index value is -1, the penultimate note is -2, and so on.
```

If you want to intercept a part of a chord/melody/track A, then just A

```python
[start position:end position]
```

and that's it. What you get is a new chord with the notes in it as the intercepted part.

For example, if chord B has 6 notes, and you want to get the first 5 notes of chord B, then you can write:

```python
B[:5]
# The ending position 6 is not included, so it corresponds to the 1st, 2nd, 3rd, 4th, and 5th notes of B
```

If you want to get the 2nd to 5th notes of chord B, then you can write:

```python
B[1:5]
# Note that here the left is closed and the right is open, which means that the ending position 5 is not included in the result, so B[1:5] is extracting the 2nd to the 5th note of B, for a total of 4 notes.
```

If you want to get the 2nd note of chord B and all the notes after it, then you can write:

```python
B[1:]
```

To get the last 3rd to the last 1st note of the chord B, write

```python
B[-3:]
```



## Raise or lower a chord

If you want to raise or lower a chord (or of course a melody or musical fragment), then you can use the up and down functions. Given a chord A, the

```python
A.up(x)
```

means to raise the overall chord A by x semitones (x can also be a negative number, which means to lower the absolute value of x by one semitone), and

```python
A.down(x)
```

means to lower the chord A by x semitones.

Advanced syntax:

```python
+A
```

means to raise the whole chord A by one semitone, as many plus signs as there are semitones, e.g.

```python
+++A
```

means raise the chord A by three semitones overall, but since the chord A will be overwritten again with each plus sign, (equivalent to A.up().up().up())

So I also devised a one-step writeup that

```python
A + 3
```

means to raise the chord A by three semitones overall, which is equivalent to A.up(3),

```python
-A
```

means to lower the overall chord A by one semitone, as many minus signs as there are semitones, e.g.

```python
---A
```

means to lower the chord A by three semitones, which is equivalent to A.down().down().down()

```python
A - 3
```

means to lower the chord A by three semitones overall, which is equivalent to A.down(3)

If you only want to raise a certain note in the chord, then just

```python
A.up(x, k)
```

or

```python
A + (x, k)
```

Lowering then is

```python
A.down(x, k)
```

or

```python
A - (x, k)
```

where k denotes the index of the note. For example

```python
get_chord('C','maj').up(1)
```

gives a new chord, each note of which is a semitone higher than the previous chord.
The notes of the chord are C#, F, G#.

```python
get_chord('C','maj').up(1,0)
```

will get a new chord with only the first note raised a semitone and the notes of the chord are C#, E, G.

If you want to raise and lower each note differently, then you can let x equal a list where each element of the list is the number of chromatic notes raised and lowered.
For example.

```python
A.up([1,2,0,-1])
```

or

```python
A + [1,2,0,-1]
```

means to raise the first four notes of the chord A by one semitone, raise them by two semitones, leave them unchanged, and lower them by one semitone.
The down case goes on like that.



## Sequencing a chord

If you want to sequence the constituent notes of a chord A, then just

```python
A.sort(x)
```

where x is a list documenting the order.
For example, if you have a minor seventh chord of A, and for its 4 constituent notes A,C,E,G you want to sort them in the order of CEAG, then write

```python
A.sort([2, 3, 1, 4])
```

and that works.

Advanced syntax:

```python
A / [2, 3, 1, 4]
```

Equivalent to A.sort([2, 3, 1, 4])



## Transpose a chord (or a piece)

If you want to transpose a melody (including the chord underlay), then you can use the modulation function. For example, if you want to transpose a piece of music A right now, then you can

```python
A.moulation(the_previous_key, the_key_to_transpose_to)
```

We'll talk about how to represent a tonic next.
For example, if you have a music clip p in the key of A major, and you want to shift to A minor, you can write:

```python
p.modulation(scale('A', 'major'), scale('A', 'minor'))
```

This will shift the music clip p from A major to A minor.



## Get the names of all notes of a chord

First, if you just get a list of the notes of chord A, then you just need

```python
A.notes
```

to get a list of the notes of chord A. For example, if A is an A minor seventh chord, then you get

```python
[A5, C6, E6, G6]
```

If you want to get a list of all the note names of the chord A, then you can use one of the built-in functions names of the chord, for example

```python
get_chord('A','m7').names()
```

and you get

```python
['A', 'C', 'E', 'G']
```



## Merge and join two chords or two musical fragments (voices merge, voices concatenate)

The built-in function `add` of the chord type can merge two chords (or two music fragments).
For example, there are two pieces of music (the chord type itself can also be a piece of music) A and B.

The parameter mode can be used to select the mode of merging.

When mode == 'head',

```python
A.add(B, mode='head')
```

You can get the new music clip after merging the two music clips A and B. The beginning of B is aligned to the beginning of A, that is, the music clip where both A and B are playing from the beginning at the same time.

The mechanism of the merge is to recalculate the interval of the merged notes, and then to reorder the notes of A and B according to the calculated interval.
The add function also has a parameter, start, which can be used to set where B should be merged from A, i.e. where the beginning of B should be aligned to A.
The unit is bars, in other words, how many bars after the beginning of A does B start to play. For example.

```python
A.add(B, mode='head', start=8)
```

You can get the merged piece of music that B plays from bar 8 of A.

Advanced syntax:

```python
A & B
A & (B, start)
```

When mode == 'tail',

```python
A.add(B, mode='tail')
```

You can get the new music clip after the music clip B is appended to the music clip A. Note, however, that this mode appends the note list of B directly to the note list of A. If the last few notes of music clip A have 0 intervals, then the beginning notes of music clip B may overlap with the last few notes of A. If you are sure that the last few notes of A are not 0 intervals, then this mode can be used safely.

When mode == 'after',

```python
A.add(B, mode='after')
```

You can get the new music clip after the music clip B is appended to the music clip A. This mode differs from the tail mode in that it specifically calculates whether more notes need to be spaced between A and B to avoid the situation where the end of A and the beginning of B overlap in some cases in the tail mode. So it is best to use this mode when you are not sure if the last few intervals of A are zero.

Advanced syntax:

```python
A | B
A + B
```



## Making changes to the notes within a chord

I've already talked about how to access the notes within a chord by index value, e.g. A[0] will give you the first note of chord A.
If you want to modify the notes within a chord, for example, if chord A is a C major seventh chord

(in the original form, C, E, G, B) We want to change the second note (third) of chord A to F, that is, turn chord A into a maj7sus4 chord, we can write it like this

```python
A[1] = 'F5'
```

Then we print the chord A, again

```python
chord(notes=[C5, F5, G5, B5], interval=[0, 0, 0, 0], start_time=0)
```

You will see that the second note of chord A has changed from E5 to F5.
Note that the changed note can be either a note type (note('A', 5) as obtained by the note initialization function) or a string representing the note.
But it must have an octave, not just the note name, like 'F' can't be used here, it must have an octave, like 'F5'.



## Deleting some notes of a chord, or inserting a new note in a certain position

You can refer to the logic of python's list, using

```python
del A[n]
```

You can delete the nth note of a chord A, using

```python
A.pop()
```

You can remove the last note of a chord A and return the last note of the chord A, using

```python
A.insert(i, b)
```

The note b can be inserted at the i-th position of the chord A

```python
A.append(b)
```

You can add the note b to the chord A
In addition, the extend, remove functions use the same logic as the built-in methods of the same name in the list.
When you want to remove a note from chord A, you can use the '-' sign to do so, for example

```python
A - 'B5'
```

If the chord A has the note B5, a new chord with the note B5 removed is returned, if not, the unmodified chord A is returned.



## Adding a lowest note to a chord (adding a bass note)

For example, if chord A is a G major chord (G major triad) with the notes G5, B5, D6, and we want to add a C note as the lowest note to the chord A.
Then we can write (the parameter could be a string or a note instance)

```python
A.on('C5')
```

The result is a new chord with C5 as the lowest note.
This is expressed as

```python
chord(notes=[C5, G5, B5, D6], interval=[0, 0, 0, 0], start_time=0)
```

Advanced syntax:

```python
A % 'C5'
```



## Find what note is the first note in a chord

For example, if the chord A is an Fmaj9 chord with the root note F5, in the original position, and you want to find what note 'E6' is in, then you can write

```python
A.index('E6')
```

The result is 3, which means that the note E is the 4th note of the Fmaj9 chord.
If the note is not in the chord, -1 is returned.
You can also omit the number of octaves and just write the name of the note to find it, returning the position of the first note with the same name, e.g.

```python
A.index('G')
```

The result is 4, which means that the note G is the fifth note of the Fmaj9 chord.



## Adding a rest to the end of a chord

If you want to add an n-bar rest to the chord A, then you can use the built-in function rest of the chord class

```python
A.rest(n)
```

which adds a rest of n bars to chord A. The result is a new chord with chord A plus a rest of n bars.

Advanced syntax:

```python
A | n
```

Regarding the current definition of rest in musicpy, rest itself is a data structure that can be constructed with `rest(duration)` and can be added to chord types, but it is only reflected in the note interval and does not exist in the note list of the chord type itself; rests are only meaningful when constructing chord types.



## Invert a note of a chord to the highest note

For example, if chord A is a C major triad in the original positions C, E, G, and you want to invert E to the highest note, then you can write

```python
A.inversion_highest(2)
```

That is, put the second note of the chord A to the highest note, and the resulting chord will have the notes C, G, E

Advanced syntax:

```python
A / -2
```

or

```python
A ^ 2
```

(A / -n means invert the nth note of chord A to the highest note)



## Invert a note of a chord to the lowest note

For example, if chord A is a C major triad in the original position C, E, G, and you want to invert E to the lowest note, then you can write

```python
A.inv(2)
```

or

```python
A.inv('E')
```

That is, putting the second note of the chord A to the lowest note gives a chord with the notes E, C, G.
Note that this is different from the normal first inversion of a C major triad (E, G, C).

Generally speaking, a chord is inversioned in the classical sense by raising the lowest note (the root note in the first inversion) by an octave.

However, a more generalized inversion requires only that the lowest note is the one inversioned.

Advanced syntax:

```python
A @ 2
```

```python
A @ 'E'
```



## Transpose all the notes of a chord to within one octave

For example, if chord A has 5 notes, and the highest ones are distributed in octaves higher than the lower ones, then

```python
A.inoctave()
```

will return a chord type that puts all the notes of chord A into the same octave, with the number of octaves being the number of octaves of the first note of chord A.



## Normalizing a chord

To normalize a chord A, you can use the standardize function

```python
A.standardize()
```

The new chord is obtained after standardizing chord A.

The definition of standardization here is

    1. If there are repeated note names within the chord (even in different octaves),
       then only the lowest pitch (smallest number of octaves) is kept.
    2. Limit all notes to within two octaves, i.e. to the 15th of the lowest note,
       and if there are any notes that are more than two octaves higher than the lowest note,
       then subtract these notes by an octave down until all the notes are within two octaves from the lowest note.
    3. Standardize all the note names into a format with no sharp and flat signs or only # signs,
       and if there are b signs, convert them to equal pitch names with # signs in the 12 equal temperament.

After standardization, the pitch of the lowest note of the chord is the same as before standardization. The chord returned is the new chord after the chord A has been normalized.



## Sorting a chord by pitch number

If the notes in a chord are not sorted by pitch, for example, if the notes of chord A are E5, C5, G5, then you can write

```python
A.sortchord()
```

The return is a new chord with the notes of chord A sorted from lowest to highest in pitch.



## Get the negative harmony of a chord according to the set scale

For example, if chord A is a Cmaj7 chord and you want to get the negative harmony of chord A with respect to the C major scale, then you can write:

```python
A = C('Cmaj7')
>>> alg.negative_harmony(scale('C', 'major'), A)
chord(notes=[G3, D#4, C5, G#4], interval=[0, 0, 0, 0], start_time=0)
```

What you get is a new chord composed of the notes of chord A about the negative harmony of the C major scale after the transformation.

Other parameters of negative_harmony function:

`get_map_dict`: when True, returns a dictionary of the notes of the first parameter scale mapped to the negative harmony.

When False, if no chord type is passed in, then the negative harmonic scale type is returned for the passed in scale type, e.g.

```python
>>> alg.negative_harmony(scale('C', 'major'))
[scale]
scale name: C4 minor scale
scale intervals: [2, 1, 2, 2, 1, 2, 2]
scale notes: [C4, D4, D#4, F4, G4, G#4, A#4, C5]
```

There is also a parameter `sort`, which, when True, will sort the notes by pitch from lowest to highest after converting the chord a to a negative harmonic version. The default value is True.



## Extracting the notes within a chord by index value, including the higher and lower octaves of the note shift

For example, if chord A is a C major triad with C5, E5, G5, we want to get a string of Alberti basses, i.e. a left-hand arpeggio accompaniment of a triad played in alternating root, fifth, third and fifth, we want to get a string of notes C5, G5, E5, G5, C6, G5, E5, G5 ( Note that the fifth note is C6, an octave above the root note, which is a typical left-hand arpeggio accompaniment of Alberti's bass. This string of notes can be easily extracted from chord A using the get function of the chord type.

```python
A.get([1, 3, 2, 3, 1.1, 3, 2, 3])
```

The result obtained is

```python
chord(notes=[C5, G5, E5, G5, C6, G5, E5, G5], interval=[0, 0, 0, 0, 0, 0, 0, 0], start_time=0)
```

Here 1, 2, 3 are the notes in chord A. The decimal numbers 1.1 indicate the number of octaves (the number before the decimal point) that the first note (the number after the decimal point) is raised.

If you want a note to be lowered by a few octaves, then just write a negative decimal number, for example -2.1 for the note after lowering the second note by one octave.

Advanced syntax:

```python
A @ [1, 3, 2, 3, 1.1, 3, 2, 3]
```



## Build a set of chord processing rules for any chord type

The easiest way to do this is to use the syntax of python's own lambda function, e.g.

Enter a chord name and then form a new chord type (a chord accompaniment) with this chord in the order of 1st note, 2nd note, 3rd note, 1st note 1 octave higher, 2nd note 1 octave higher, 3rd note, 1st note 1 octave higher, 2nd note 1 octave higher, and then set the duration of each note of the chord accompaniment to 0.5 bars and the interval of each note to 0.5 bars, and repeat the chord accompaniment twice.

```python
rules = lambda x: C(x) @ [1, 2, 3, 1.1, 2.1, 3, 1.1, 2.1] % (1/8, 1/8) * 2
```

Now we can use the chord processing rules rules to process the C major triad, the C7sus4 chord, the G7/B chord, and the C major triad, and then connect them with the '|' sign to form a little piece of music.

```python
A = rules('Cmajor') | rules('C7sus4') | rules('G7/B') - database.octave | rules('Cmajor')
```

Play part A at 115 BPM (speed)

```python
play(A, 115)
```

Get the 1st inversion of a chord type, and then set the note durations of the chords to 1/4, 1/2, 1/2 (in bars), respectively.

```python
rules = lambda x: (x / 1) % ([1/4, 1/2, 1/2], [1/4, 1/4, 1/2])
```



## View note interval list and note duration list for a chord type

```python
a = C('Dmaj7')

## View a list of note intervals for a chord type
>>> print(a.interval)
[0, 0, 0, 0]

# View a list of note durations for a chord type
>>> print(a.get_duration())
[0.25, 0.25, 0.25, 0.25]
```



## View note volume list for a chord type

```python
a = C('Dmaj7')
a.set_volume([80,80,100,100])

# View a list of note volumes for a chord type
>>> print(a.get_volume())
[80, 80, 100, 100]
```



## Another way to set the volume of a chord type

```python
# You can use the set_volume method to set the volume of a chord type
a = C('Emaj7')
a.set_volume(80)
# You can also use the set function or the advanced syntax % to set the volume as the third argument after the first note duration and interval
a = a.set(1/8,1/8,80)
a = a % (1/8,1/8,80)
```



## Get only note types of a chord type

If you want to keep only the note types of a chord type and remove all other types (such as tempo types, pitch_bend types, etc.), then you can use the built-in function `only_notes`.

```python
a, bpm, start_time = read('example.mid').merge()
a = a.only_notes()
```



## Get the chord type according to the guitar's fret count and guitar tuning standard

You can use the `guitar_chord` function from algorithm module to get the chord type by the number of frets of the guitar's 6 strings and the guitar's string standard (which can be left unset, the default is the standard 6 string guitar tuning)

```python
guitar_chord(frets,
             return_chord=True,
             tuning=['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
             duration=0.25,
             interval=0,
             **detect_args)
# frets: A list of the number of frets from the lowest to the highest note of the 6 strings of your guitar, the number of frets is an integer, if it is an empty string write 0, if it is a non-playing string write None
# return_chord: Whether or not to return the chord type, if False it will determine what chord is played by the number of frets you pressed and return the specific chord name, default is True.
# tuning: the tuning of the guitar, the default value is the standard tuning of a 6-string guitar, you can also customize the tuning of your guitar
# duration: a list of note durations for the type of chord returned
# interval: A list of note intervals for the chord type
# detect_args: parameters to determine the specific type of chord, i.e. parameters of the detect function, set by keyword parameters

# For example, if a standard guitar C major triad in the first three frets is 3 frets on the 5th string, 2 frets on the 4th string, 3 frets on the 3rd string, 1 frets on the 2nd string, and 1 frets on the 1st string, then you can write
>>> alg.guitar_chord([None, 3, 2, 0, 1, 0])
chord(notes=[C3, E3, G3, C4, E4], interval=[0, 0, 0, 0, 0], start_time=0)
>>> alg.guitar_chord([None, 3, 2, 0, 1, 0], return_chord=True)
'Cmajor'
```



## Calculate the actual playing time of a chord type according to the specified BPM

You can use the built-in function `eval_time` to calculate the actual playing time of a chord type by specifying a BPM

```python
a = C('Cmaj7') | C('Dm7') | C('E9sus') | C('Amaj9', 3)
>>> a.eval_time(80)
'3.0s'

eval_time(bpm,
          ind1=None,
          ind2=None,
          mode='seconds',
          start_time=0,
          normalize_tempo=False,
          audio_mode=0)

# bpm: the specified speed BPM

# ind1, ind2: select the bar interval, 0 as the first bar, if not set then default to the whole song

# mode: you can choose 'seconds' to return the string of time in seconds,
# or 'hms' to return the string of time in hours, minutes, seconds,
# or 'number' to return the float of time in seconds

# start_time: the start time of the chord

# normalize_tempo: whether to normalize tempo changes or not

# audio_mode: refer to the parameter of bars function
```



## Slicing chord types by range of bars

If we want to extract a slice of a chord type from bar 6 to bar 8, we can use the built-in function ``cut``

```python
cut(ind1=0,
    ind2=None,
    start_time=0,
    cut_extra_duration=False,
    cut_extra_interval=False,
    round_duration=False,
    round_cut_interval=False)

# ind1, ind2: the range of the number of bars to extract, ind2 if not set, then extract to the end, ind1 default value is 0, that is, from the beginning of bar 0 to extract

# start_time: When reading a MIDI file, the notes of a MIDI channel will have their own start time, which can be set here as a chord type delay, the unit here is bars

# cut_extra_duration: the cut function by default includes all notes that start within the specified bar range (excluding the right endpoint), independent of note length, so there may be cases where the note length exceeds the bar range, if set to True, then the note length of notes that exceed the bar range will be adjusted

# cut_extra_interval: if set to True, adjust the note intervals that exceed the bar range

# round_duration: if set to True, remove the note when the adjusted note duration has a very small value

# round_cut_interval: if set to True, when calculating the interval, if it is very close to ind2, round the interval to ind2

# The cut function returns a new chord type with a slice in the range of the specified number of bars

a.cut(6, 8)

# Extracts the part of the chord type a from the 6th bar to the 8th bar (from the beginning of the 6th bar to the beginning of the 8th bar)
```



## Calculate the total number of bars of a chord type

Use the built-in function ``bars`` to get the total number of bars of a chord type

```python
bars(start_time=0,
     mode=1,
     audio_mode=0,
     bpm=None)

# start_time: additional start time

# mode: if 0, calculated as the sum of all note intervals; if 1, calculated as the maximum distance the notes in the chord can reach, taking note duration into account (without taking the last note interval into account); if 2, taking the last note interval into account in the case of 1

# audio_mode: if 1, the time length of the pydub AudioSegment instance in the note list is converted to the note length

# bpm: bpm when calculating the note length corresponding to the time length of the pydub AudioSegment instance

a = C('Cmaj7') | C('Dm7') | C('E9sus') | C('Amaj9', 3)
>>> a.bars()
1.0
```



## Slice chord types according to the range of realistic playing times

Using the built-in function `cut_time`, specifying a BPM, you can select a time range for slicing chord types.  
For example, if chord type a is played at 100 BPM, and the part from the 10th to the 20th second is extracted, you can write

```python
a.cut_time(100, 10, 20)
# If the right side of the range is not set, then it will extract to the end by default, and the left side will default to extract from the very beginning
```



## Extract the first n bars of a chord type

```python
a.firstnbars(n)
```



## Extract the part of a chord type for a particular bar

```python
a.get_bar(n)
```



## Extract the contents of each bar of a chord type

```python
a.split_bars()
# You can get a list of chord types consisting of parts of each bar of the chord type a
```



## Count the number of occurrences of a note name within a chord type

```python



## If you want to get the number of occurrences of the note named F# in chord type a, you can write
a.count('F#')
# You can also specify the number of octaves and count only the notes with the same name and octave
a.count('F#5')
```



## Get the most occurrences of a chord type

```python
a.most_appear()



## The choices parameter sets which notes to select from, if not it defaults to all 12 notes
```



## Unify all sharp and flat signs of notes of a chord type

```python
# Let's say a chord type has notes C5, Eb5, G5, A#5, D#6, Bb6, F5 (a random melody).
# If we want to unify the notes with a rising and falling sign,
# convert all the notes with a falling sign to the equivalent of the notes with a rising sign in pitch
# that is, C5, D#5, G5, A#5, D#6, A#6, F5, then we can write
a = chord('C5, Eb5, G5, A#5, D#6, Bb6, F5')
>>> print(a)
chord(notes=[C5, Eb5, G5, A#5, D#6, Bb6, F5], interval=[0, 0, 0, 0, 0, 0, 0], start_time=0)
a = a.standard_notation()
>>> print(a)
chord(notes=[C5, D#5, G5, A#5, D#6, A#6, F5], interval=[0, 0, 0, 0, 0, 0, 0], start_time=0)
```



## Re-quantize the chord type with note duration and note interval according to the tempo change inside

For example, now we have a chord type that holds a piece with some tempo types (tempo change types), i.e. different parts of a piece will have different tempos. If we want to unify the tempo of the whole piece, but still want to keep the different tempos of the previous parts, then we need to re-quantize the different tempos of each part in proportion to the tempo we want to unify If we want to unify the tempo of the whole piece, but still want to keep the different tempo of the previous parts, then we need to recalculate the note duration and note interval of each part in proportion to the different tempo of each part relative to the desired unified tempo. In some classical music MIDI files, there are many complex, frequent, fast and subtle tempo changes, and unifying the tempo of the whole piece can facilitate the music theory processing afterwards, because unifying the tempo is equivalent to recalculating the note durations and note intervals of each part to the actual equivalent of the relatively unified tempo. The note durations and note intervals of each tempo are recalculated to their actual equivalents, which facilitates algorithmic processing during the analysis of the music theory (since there is no need to consider the actual playing time changes due to tempo changes in each part)

```python
# Use the built-in function normalize_tempo to re-quantize notes according to the tempo change type stored in a chord type.
# The normalize_tempo function supports both chord types (chord types) and piece types (piece types)
a = read('example.mid') # a is the piece type converted to after reading the MIDI file example.mid
a.normalize_tempo() # parameter bpm, default value is None, if bpm is None, use the tempo parameter that comes with the piece type
a.normalize_tempo(100) # set bpm to 100, unify bpm to 100 for the whole piece, re-quantize each part of the notes

b, bpm, start_time = read('example.mid').merge() # b is the chord type after reading the MIDI file example.mid and merging all the tracks
b.normalize_tempo(bpm=100, start_time=0) # The bpm parameter is the tempo you want to normalize, and the start_time parameter is the time in bars when the chord type starts playing, the default is 0
# Here we unify the speed of the chord type b to 100 BPM
```



## Calculating the range of bars between two indices in a chord type

Using the built-in function `count_bars` of a chord type, you can calculate the range of bars between two indices, for example, if there is a chord type with 100 notes.  
We want to calculate the range of bars between the 2nd note and the 10th note, i.e. the range that starts with the number of bars where the 2nd note is and ends with the number of bars where the 10th note is.  
Or maybe we want the number of bars (the range of bars) that pass between the 2nd note and the 10th note. We can write it like this.

```python
count_bars(ind1, ind2, bars_range=True)
# ind1, ind2 is the index (the first note) of the beginning and ending note, as an integer
# ind1 is the index of the first note, and bars_range is True, which returns the range of bars as a list [number of starting bars, number of ending bars]
# False returns the length of the bars elapsed between the two indices, the value is a numeric value
a = chord('A5, B5, C6, G5, G#5, ...') % (duration, interval) # chord a has 100 notes
bar_length = a.count_bars(2, 10)
>>> print(bar_length)
[1.5, 7.5]
bar_length = a.count_bars(2, 10, False)
>>> print(bar_length)
6
# The values here are for example only
```



## Building a chord progression

Earlier, when talking about the basic syntax of scale types, it was mentioned that scale types can extract chord progressions by steps, so if you are generating chord progressions directly from the perspective of chord names, you can use the `chord_progression` function, which is a global function and does not require any musical type as a prerequisite.

```python
chord_progression(chords,
                  durations=1 / 4,
                  intervals=0,
                  volumes=None,
                  chords_interval=None,
                  merge=True,
                  scale=None,
                  separator=',')
'''
chords: string of chord names or a list of chord types, where chord names can also be meta-tuples of C function arguments

durations: the duration of each chord, either as a value or as a list

intervals: the interval of each chord, either as a value or as a list

volumes: default volume of each chord, can be a value or a list, if None, no setting

chord_interval: the interval between each chord, can be a value or a list

merge: if True, returns the chord type after merging all chords in the chord progression, if False, returns a list of chord types in the chord progression

scale: you can set a scale type for scale degrees extractions, please refer to chord_progreession function of scale type

separator: when chords is a string, separate each chord with the separator string
'''

chord_progression_example = chord_progression(['F', 'G', 'Am', 'Em'])
chord_progression_example = chord_progression([('F',4), ('G',4), ('C',5), ('Am',4)])
chord_progression_example = chord_progression([C('F')^2, C('G')^2, C('Am')^2, C('Em')^2])
>>> print(chord_progression_example)
chord(notes=[F4, C5, A5, G4, D5, B5, A4, E5, C6, E4, ...], interval=[0, 0, 1/4, 0, 0, 1/4, 0, 0, 1/4, 0, ...], start_time=0)
# If there is a higher requirement for the arrangement of the notes of each chord (such as inversion or playing in a certain pattern of note arrangement, etc.), it is recommended to pass in the chord type, and the chord type can also be written directly to the melody.
# If it is a string it is limited to the range that the C function can parse.
```



## View information about the musical analysis of a chord type

Using the built-in function `info` for chord types, you can view the chord type, root note, and chord peculiarities (root position, inversion, polychord, etc.) of a chord type's notes, as well as omitted notes, altered notes, chord voicings, non-chord bass note if it has. If the chord instance does not contain a chord, which means it contains only a note or interval, the info will show the note name or interval name.

```python
>>> print(chord('A,C,F').info())
chord_type(root='F', chord_type='major', chord_speciality='inverted chord', inversion=1, omit=None, altered=None, non_chord_bass_note=None, voicing=None, type='chord', note_name=None, interval_name=None, polychords=None, order=[2])

>>> print(chord('A').info())
chord_type(root=None, chord_type=None, chord_speciality='root position', inversion=None, omit=None, altered=None, non_chord_bass_note=None, voicing=None, type='note', note_name='A4', interval_name=None, polychords=None, order=None)

>>> print(chord('C,E').info())
chord_type(root='C', chord_type=None, chord_speciality='root position', inversion=None, omit=None, altered=None, non_chord_bass_note=None, voicing=None, type='interval', note_name=None, interval_name='major third', polychords=None, order=None)
```



## Getting a chord type for a sus

If we want to get a chord type sus4 or a variant of sus2, then we can use the built-in `sus` function of the chord type, which defaults to 4

```python
a1 = chord('C, E, G')
>>> print(a1.sus())
chord(notes=[C4, F4, G4], interval=[0, 0, 0], start_time=0)
>>> print(a1.sus(2))
chord(notes=[C4, D4, G4], interval=[0, 0, 0], start_time=0)
# The sus function can take 2 or 4 as arguments, and sus a chord type with a 3rd for the lowest note, replacing it with a 2nd or 4th note.
# Not only for triads, but also for more complex chords such as 7th, 9th, 11th, etc.
```



## Delay the same chord type n times or play it n times at intervals

Recently, the syntax to delay a chord type n times and play it n times at intervals has been added, using the `&` and `|` symbols, respectively.
These two symbols are used to play a chord type simultaneously or sequentially with another chord type, but now if you pass in an tuple then you can get the result of repeating the same chord type with a delay.

```python
a1 = chord('C, E, G')
>>> print(a1 & (3, 1/8)) # Play the chord type a1 3 times, each time with 1/8 more bars of delay than the beginning
chord(notes=[C4, E4, G4, C4, E4, G4, C4, E4, G4], interval=[0, 0, 1/8, 0, 0, 1/8, 0, 0, 1/4], start_time=0)

>>> print(a1 | (3, 1/8)) plays the chord type a1 3 times, each time after the other, but with an interval of 1/8 of a bar first
chord(notes=[C4, E4, G4, C4, E4, G4, C4, E4, G4], interval=[0, 0, 3/8, 0, 0, 3/8, 0, 0, 0], start_time=0)
```



## Unify accidentals of chord type

You can use the chord type `same_accidentals` function to unify the ascending and descending notes of a chord type,

```python
a = chord('C5, D#5, F5, Ab5, E5, D5, C#5')
>>> a.same_accidentals('#')
chord(notes=[C5, D#5, F5, G#5, E5, D5, C#5], interval=[0, 0, 0, 0, 0, 0, 0], start_time=0)
>>> a.same_accidentals('b')
chord(notes=[C5, Eb5, F5, Ab5, E5, D5, Db5], interval=[0, 0, 0, 0, 0, 0, 0], start_time=0)
```



## Filter the notes that meet the specified conditions in the chord type

You can use the `filter` function of the chord type to filter out the notes that do not meet the conditions in the chord type by specifying conditions, and filter the notes that meet the specified conditions in the chord type.
For example, filter notes with a volume between 20 and 80, notes with a note duration between 1/16 bar and 1 bar, notes with a pitch between A0 and C8, and so on. You can also specify a function to operate on the filtered notes.

```python
filter(self, cond, action=None, mode=0, action_mode=0)

# cond: The filter condition function must be a function whose parameter is a note and the return value is a Boolean value. It is recommended to use the lambda function

# action: Operation function, if it is not None, the operation of this function is performed on the filtered notes, but the filtered notes are not extracted separately.
# Returns the modified chord type, if it is None, it returns the chord type composed of the filtered notes and the start time of the first filtered note

# mode: If it is 1, it returns the index list of the filtered notes

# action_mode: If it is 0, the return value of the action function will replace the note it is acting on. If it is 1, the action function will directly act on the note.

a = chord('C, E, G, B') # Initialize a chord
a.set_volume([10, 20, 50, 90]) # Set the volume of the note
>>> a.filter(lambda s: 20 <= s.volume < 80) # Filter the notes with a volume between 20 and 80 in the chord type
(chord(notes=[E4, G4], interval=[0, 0], start_time=0), 0) # Return the chord type composed of the filtered notes and the start time of the first filtered note

# For notes with a volume between 20 and 80, the volume is set to 50
b = a.filter(lambda s: 20 <= s.volume < 80, action=lambda s: s.set_volume(50), action_mode=1)
>>> b
chord(notes=[C4, E4, G4, B4], interval=[0, 0, 0, 0], start_time=0) # Return the chord type whose volume is modified by the action function
>>> b.get_volume() # Get the volume of the new chord type
[10, 50, 50, 90] # The volume of the notes between 20 and 80 are now 50
```



## Filter the notes within the specified pitch range of the chord type

You can use the `pitch_filter` function of the chord type to filter the notes within the specified pitch range of the chord type. This function is very important in many occasions, such as when you read a MIDI file,
It is necessary to map the notes of the MIDI file to a piano in the software for display. Generally speaking, the piano has 88 keys and the pitch range is A0 ~ C8, but the MIDI file can store notes that exceed this pitch range.
It may be lower than A0 or higher than C8, so we need to limit the pitch of the notes of the read MIDI file to between A0 and C8, and the notes that do not belong to this range need to be removed. This function can do this,
And it will recalculate the interval of all the notes after filtering, so it will not affect the position of the notes when outputting to MIDI files again. The more generalized `filter` function also recalculates the interval of all notes.

```python
pitch_filter(self, x='A0', y='C8')

# x: The lowest pitch of the pitch range, the default value is A0

# y: The highest pitch of the pitch range, the default value is C8

a = chord('Ab0, C5, E5, G5, B5, G10') # this is a chord with 2 notes that the pitches do not belong to A0 ~ C8
>>> a.pitch_filter() # Use the default pitch range A0 to C8 to filter the notes of the chord type
(chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0), 0)
# Return the chord type composed of the filtered notes within the specified pitch range, and the start time of the first filtered note

b = chord('Ab0, C5, E5, G5, A5, C7, G10')
>>> b.pitch_filter('C5','C6') # Filter the notes whose pitch is between C5 and C6
(chord(notes=[C5, E5, G5, A5], interval=[0, 0, 0, 0], start_time=0), 0)
# Return the chord type composed of the filtered notes within the specified pitch range, and the start time of the first filtered note
```



## Find a certain degree of a chord type

Now, for example, you have a C minor eleventh chord, and you want to get its 3rd and 9th degrees. At this time, you can use the `interval_note` function of the chord type and enter a degree to find it. If the current chord type does not contain notes of the specified degree, then `None` will be returned. The number of degrees supported for search includes from 1 degree (root note) to 13 degrees, as well as the case of changing sounds, such as `#5`, `b9`.

```python
interval_note(self, interval, mode=0)

# interval: The degree you want to find, it can be an integer or a string representing the degree

# mode: When it is 0, if the note of the specified degree cannot be found, None will be returned. When it is 1, the starting note of the chord type plus the note type of the specified degree will be returned.

>>> C('Cm11') # C minor eleven chord
chord(notes=[C4, D#4, G4, A#4, D5, F5], interval=[0, 0, 0, 0, 0, 0], start_time=0)

>>> C('Cm11').interval_note(3) # Find the 3rd note of the C minor eleventh chord
D#4 # Return to the 3rd of the C minor eleventh chord. If it is more musically rigorous, it should be Eb4.
# The reason why this is D#4 is because musicpy’s default note representation is to give priority to the # number

>>> C('Cm11').interval_note(9) # Find the 9th note of the C minor eleventh chord
D5 # Returns the 9th degree of the C minor eleventh chord

>>> C('Cm11').interval_note(d5, mode=1) # Returns the first 5th of the C minor eleventh chord,
# Note that the degree here cannot be a string, because the note type plus the string will be interpreted as forming a chord type
F#4 # Return to the first note of the C minor eleventh chord with a 5th falling pitch (here, strictly speaking, it should be Gb4, for the same reason as before)
```



## Confirm that a note is what degree of a chord

What is done here is the reverse of `Find a certain degree of a chord type`. You can use the `note_interval` function of the chord type to confirm the degree of a note in a chord type.
If the specified note is not in the chord type, the relationship between the initial note of the chord type and the degree of this note will also be returned.

```python
note_interval(self, current_note, mode=0)

# current_note: The note whose degree you want to confirm, it can be a string or a note type

# mode: When it is 0, it will return the degree expressed by the rise and fall signs and numbers, when it is 1, it will return to the pure English interval representation

>>> C('Cm11') # C minor eleven chord
chord(notes=[C4, D#4, G4, A#4, D5, F5], interval=[0, 0, 0, 0, 0, 0], start_time=0)

>>> C('Cm11').note_interval('Eb4') # Confirm that the note Eb4 is a few degrees of the original C minor eleventh chord starting with C4
'b3' # The returned result is 3 degrees (b3 means 3 degrees lower, or 3 degrees lower, because the 3 degrees that are not lowered are 3 degrees higher)

>>> C('Cm11').note_interval('D5') # Confirm that the note D5 is a few degrees of the original C minor eleventh chord starting with C4
'9' # The returned result is 9th (large 9th)

>>> C('Cm11').note_interval('Db5') # Confirm that the note Db5 is a few degrees of the original C minor eleventh chord starting with C4
'b9' # C minor eleventh chord does not include the note Db, but this function will also return the interval relationship formed by the initial note C4 and Db5 of the chord, which is b9 (lower nine degrees or minor nine degrees)

>>> C('Cm11').note_interval('D5', mode=1) # Confirm that the note D5 is a few degrees of the original C minor eleventh chord with C4 as the starting note, and return to the pure English representation
'major ninth'
```



## Obtain the chord voicing according to the degree of the chord

There are many ways to arrange and combine the notes of a chord. Each unique combination is a kind of voicing. By placing the notes of the chord in different orders and octaves, a chord can have various voicings, each kind of voicing has a unique sense of hearing, whether it is columnar chords, split chords or arpeggios, you can hear different tastes. For example, a Cm11 chord can be played in the order of 1, 3, 5, 7, 9, and 11th degree in the original position.
You can also follow the order of 1, 5, 9, 3, 7, and 11th degree to create a more dreamy and beautiful sense of hearing. Therefore, we need a convenient function to obtain a chord's voicing by the degree of the chord, including the order of the sound, the omission of the sound, and the repetition of the sound in a higher octave all need to be considered. The chord type's `get_voicing` function I designed recently can do this.

```python
get_voicing(self, voicing)

# voicing: A list of chord vocal positions, that is, a list that indicates the order of the degree of the chord. The element can be an integer or a string indicating the degree

# It should be noted that the chord vocal position list must all have the degrees of the current chord type

>>> C('Cm11').get_voicing([1,5,9,3,11,7]) # C minor eleventh chord according to root, 5th, 9th, 3rd, 11th, 7th degree,
# and redistribute the octaves of all notes according to the rule that the following notes are higher than the preceding notes
chord(notes=[C4, G4, D5, D#5, F5, A#5], interval=[0, 0, 0, 0, 0, 0], start_time=0)
# Return to the voicing chord type of the C minor eleven chord arranged according to the specified chord vocal position list

play(C('Cm11').get_voicing([1,5,9,3,11,7])% (1, 1/8), 150) # Play with fast arpeggios
```



## Adjust the notes of the current chord type to a place closer to the notes of another chord type

When considering the arrangement of chord parts, if you want a smoother connection between the next chord and the previous chord, then one of the ways is to place the sound of the next chord closer to the sound of the previous chord, in this way, the connection of different parts in a chord progression will be smoother, because the movement of the parts is relatively small.

For example, the original position of the Am chord is connected to the original position of the F chord, that is, A C E is connected to F A C. If you want to connect these two chords more smoothly, you can adjust the order of the notes of the F chord so that each note of the F chord is as close as possible to the original position of the Am chord. For example, adjust it to ACF so that the first two notes of the F chord are in the original position of the Am chord. The first two notes of are the same, the third note F is only one semitone higher than the original third pitch of the Am chord, so the two chords connected will sound smoother and smoother.

You can use the `near_voicing` function of a chord type to adjust the sound of the current chord type to the order of the pitch of another chord type. If the pitch difference between the two chords is relatively large, then it will also move the pitch of the current chord type to the pitch range of another chord type.

You can also fix the lowest note of the current chord type without adjusting the closest pitch distance, because sometimes the lowest note changes, the chord inversion obtained is not what we want.

```python
near_voicing(self,
             other,
             keep_root=True,
             standardize=True,
             choose_nearest=False,
             get_distance=False)

# other: The chord type used as a standard for adjusting the pitch of the current chord type

# keep_root: When it is True, keep the lowest note of the current chord type after the adjustment is still the lowest note

# standardize: whether to standardize the notes

# choose_nearest: if set to True, choose the one with the minimum distance between keep root and not keep root

# get_distance: if set to True, return (result, distance)

>>> C('F').near_voicing(C('Am'), keep_root=False) # Get the voicing of the closest distance to the original position of the F chord with respect to the original position of the Am chord, without keeping the lowest pitch
chord(notes=[A4, C5, F5], interval=[0, 0, 0], start_time=0)

# Write a smooth voice type connection of the 2516 chord progression in C major
chord1 = C('Dm7', 3).get_voicing([1, 7, 3])% (1,[1/4,1/4,1/2])
chord2 = C('G7, omit5', 4).near_voicing(chord1, keep_root=True)% (1,[1/4,1/4,1/2])
chord3 = C('Cmaj7, omit5', 4).near_voicing(chord1, keep_root=True)% (1,[1/4,1/4,1/2])
chord4 = C('Am7, omit5', 4).near_voicing(chord1, keep_root=True)% (1,[1/4,1/4,1/2])
play(chord1 | chord2 | chord3 | chord4, 165)
```



## Make arpeggios quickly

New in August 2021 is the function `arpeggio` to quickly create chord arpeggios. You can specify the chord type, the octave range of the chord arpeggio, the note duration and the note interval, and you can choose to play either the top line arpeggio or the bottom line arpeggio, or both. You can also use `arp` as shorthand.

```python
arpeggio(chord_type,
          start=3,
          stop=7,
          durations=1 / 4,
          intervals=1 / 32,
          first_half=True,
          second_half=False)

# chord_type: String indicating the chord type, either using the syntax supported by the C function, or the chord type

# start: the number of octaves the chord arpeggio starts in

# stop: the number of octaves the chord arpeggio ends in

# durations: note duration of the chord arpeggio

# intervals: note intervals of the chord arpeggio

# first_half: the chord arpeggio that generates the top line

# second_half: generates the lower chord arpeggio

Cmaj7_arpeggio = arpeggio('Cmaj7')

>>> Cmaj7_arpeggio
chord(notes=[C3, E3, G3, B3, C4, E4, G4, B4, C5, E5, ...], interval=[1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, ...], start_time=0)

Cmaj7_arpeggio = arp('Cmaj7', 3, 6)

>>> Cmaj7_arpeggio
chord(notes=[C3, E3, G3, B3, C4, E4, G4, B4, C5, E5, ...], interval=[1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, 1/32, ...], start_time=0)
```



## Reset the overall octave of chord type

You can use the `reset_octave` function to set the overall octave of a chord type to the octave of the 1st note of the chord type and move the chord type to the octave you set, returning a new chord type. This method is useful in cases where you don't know the overall octave of the original chord.

```python
a = C('Cmaj7', 5)

>>> a
chord(notes=[C5, E5, G5, B5], interval=[0, 0, 0, 0], start_time=0)

b = a.reset_octave(3)

>>> b
chord(notes=[C3, E3, G3, B3], interval=[0, 0, 0, 0], start_time=0)
```



## Construct chord types with other MIDI messages

Generally, you can pass in the `other_messages` attribute to add other MIDI messages when building a chord type, but if you want to add other MIDI messages after the chord type is built, you can either set the `other_messages` attribute of the chord type directly, or you can use the chord type's `with_other _messages` function to get a new chord type with additional MIDI messages. Note that `other_messages` is a list of other MIDI messages.

```python
a = C('Cmaj7')

b = a.with_other_messages([event('control_change', control=1, value=50)])

>>> b.other_messages

[event(type=control_change, track=0, start_time=0, control=1, value=50)]
```



## Write chord types by polyphony

You can use the `multi_voice` function to combine multiple chord types as multiple voices, returning the new chord type after the multiple voices are combined. This method is useful when writing polyphonic melodies and harmonies for the same instrument, such as when writing A cappella and complex drums.

```python
multi_voice(*current_chord, method=chord, start_times=None)

# *current_chord: you can pass in any number of chord types as voices

# method: If you pass in a string that represents a chord, you can choose the syntax of the chord parsing here, you can choose chord, translate and drum

# start_times: a list of the start times of the chord types after the first chord type.
# If you want to set the start times of the other voices after the first chord type relative to the first chord type, you can set this parameter in bars

a = multi_voice(chord('C2') % (1, 1) * 2,
                C('G') % (1/8, 1/8) * 4)

>>> a
chord(notes=[C2, G4, B4, D5, G4, B4, D5, G4, B4, C2, ...], interval=[0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 0, ...], start_time=0)
```



## Concatenate chord types in a list

You can use the `concat` function to merge all the chord types in a list by specifying a merge method, resulting in a new merged chord type.

```python
concat(chordlist, mode='+', extra=None, start=None)

# chordlist: list of chord types to merge

# mode: mode of concatenation, can receive values '+', '|', '&', the first 2 values correspond to 'after', the third value corresponds to 'head', the default value is '+'

# extra: extra interval to be added when merging two adjacent chord types, in bars

# start: The start value of the concatenation, if it is None, then use the first element of the list as the start value

chord_list = [C('C'), C('D'), C('E')]
>>> chord_list
[chord(notes=[C4, E4, G4], interval=[0, 0, 0], start_time=0), chord(notes=[D4, F#4, A4], interval=[0, 0, 0], start_time=0), chord(notes=[E4, G#4, B4], interval=[0, 0, 0], start_time=0)]

combined_chord = concat(chord_list, '|')

>>> combined_chord
chord(notes=[C4, E4, G4, D4, F#4, A4, E4, G#4, B4], interval=[0, 0, 1/4, 0, 0, 1/4, 0, 0, 0], start_time=0)
```



## Distribute multiple notes evenly in proportion to their length to the specified bar length

You can use the `distribute` function to distribute multiple notes evenly over a specified bar length in proportion to their length. This is useful when writing special rhythmic patterns and polyrhythms.

```python
distribute(current_chord,
           length=1 / 4,
           start=0,
           stop=None,
           method=translate,
           mode=0)

# current_chord: string or list of notes representing the chord

# length: total length of the chord to be assigned, in bars

# start: index of the note in the chord to start assigning, starting from 0, default starts from the 1st note

# stop: index of the end note of the chord to be assigned, starting from 0 and ending with the last note if it is None, default is None

# method: The method used to parse the chord when the string is passed in, the default value is translate, you can choose chord, translate

# mode: when 0, the notes are equally distributed in proportion to their respective lengths and intervals to the specified bar length.
# with 1, the note interval takes the same value as the note duration.

# Distribute the 5 notes of the Cmaj9 chord evenly over 1/2 bar length, with the same note duration and interval for the 5 notes before distribution
a = distribute(C('Cmaj9') % (1/8, 1/8), 1/2)

>>> a
chord(notes=[C4, E4, G4, B4, D5], interval=[1/10, 1/10, 1/10, 1/10, 1/10], start_time=0)

>>> a.get_duration()
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Distribute the note durations of 2 notes in 2 cents, 2 notes in 4 cents respectively (repeated 2 times) evenly over 1/2 bar length
b = distribute('C[.2;.] , D[.4;.] , r:2', 1/2)

>>> b
chord(notes=[C4, D4, C4, D4], interval=[1/6, 1/12, 1/6, 1/12], start_time=0)

>>> b.get_duration()
[0.16666666666666666666666, 0.08333333333333333, 0.16666666666666666666666, 0.0833333333333333333]
````



## Use translate function to write chord types according to drum syntax

As mentioned in the chapter of drum type, you can use the `translate` function to apply drumming syntax to notes, enabling you to write chord types in drumming syntax. Here's a more detailed explanation. One of the differences between the `translate` function and the drum type construction is that the default note interval for the `translate` function is 0, while the default note interval for the drum type is 1/8, and the default note duration for both the `translate` function and the drum type is 1/8. The default note duration, interval and volume could be set using the same parameters when initializing the drum type. The relative pitch syntax is also supported. Here I will give a few examples of using the `translate` function to write chord types.

```python
>>> translate('A2[l:1; i:1; r:2], i:1, D3[l:1; i:1; r:2]')
chord(notes=[A2, A2, D3, D3], interval=[1, 2, 1, 1], start_time=0)

>>> translate('C5[l:.8; i:.; r:3], D5[l:.16; i:.; r:2], E5[l:.8; i:.], r:2')
chord(notes=[C5, C5, C5, D5, D5, E5, C5, C5, C5, D5, ...], interval=[1/8, 1/8, 1/8, 1/16, 1/16, 1/8, 1/8, 1/8, 1/8, 1/16, ...], start_time=0)

>>> translate('C5, E5, G5')
chord(notes=[C5, E5, G5], interval=[0, 0, 0], start_time=0)
```



## Reset the overall pitch of chord types

You can use the `reset_pitch` function of a chord type to move the overall pitch of the chord type to another pitch, using the 1st note of the chord type as the standard, and the return is a new chord type. The argument can be a string representing a note or a note type. For example a Cmaj7 chord that you want to move to an Emaj7 chord, but you don't want to use `up` or `+` to do the shifting because it requires counting the number of semitones from C to E, then you can use this method.

```python
a = C('Cmaj7')

>>> a
chord(notes=[C4, E4, G4, B4], interval=[0, 0, 0, 0], start_time=0)

>>> a.reset_pitch('E')
chord(notes=[E4, G#4, B4, D#5], interval=[0, 0, 0, 0], start_time=0)

>>> a.reset_pitch('E3')
chord(notes=[E3, G#3, B3, D#4], interval=[0, 0, 0, 0], start_time=0)
```



## Chord type extracts notes from the index list to form a new chord type

When you have picked some notes from the chord type by index and want to take them out, but still want to keep the distance relationship between the original notes, then you can use the `pick` function of the chord type, which returns a new chord type composed of the extracted notes.

```python
pick(indlist)

# indlist: a list of the indices of the notes
```



## Replace notes and chords in a chord type

To replace a note in a chord type with index, you can simply write `a[index] = new_note`, where `a` is a chord type.

To replace a chord in a chord type, which is to replace multiple notes in a chord type, you can use `replace_chord` function of the chord type to replace the notes between 2 indices.

```python
replace_chord(ind1, ind2=None, value=None, mode=0)

# ind1: the start index

# ind2: the end index, if set to None, then it will be calculated as `ind1 + len(value)`

# value: the chord to replace, could be a chord type or any data structures that `chord` function could parse

# mode: if set to 0, the notes and intervals between ind1 and ind2 will be replaced by the notes and intervals of the new chord type,
# if set to 1, only the note pitch will be replaced, other attributes of the notes between ind1 and ind2 and the intervals remain unchanged

a = chord('C5, D5, E5, F5, G5, A5, B5', interval=1/8)

>>> a
chord(notes=[C5, D5, E5, F5, G5, A5, B5], interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8], start_time=0)

a.replace_chord(ind1=1, value=C('A', duration=2))

>>> a
chord(notes=[C5, A4, C#5, E5, G5, A5, B5], interval=[1/8, 0, 0, 0, 1/8, 1/8, 1/8], start_time=0)

>>> a.get_duration()
[0.25, 2, 2, 2, 0.25, 0.25, 0.25]

b = chord('C5, D5, E5, F5, G5, A5, B5', interval=1/8)

>>> b
chord(notes=[C5, D5, E5, F5, G5, A5, B5], interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8], start_time=0)

b.replace_chord(ind1=1, value=C('A'), mode=1)

>>> b
chord(notes=[C5, A4, C#5, E5, G5, A5, B5], interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8], start_time=0)

>>> b.get_duration()
[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
```


# COMPOSITION EXAMPLES

## Touhou Project main theme

```python
play((get_chord_by_interval('D#4', [5,7,10,7,5], 1/2, 1/8)*3 + get_chord_by_interval('F4', [1,0,-4], 1/2, 1/8)) * 3, 150)
```

## Play the A minor seventh chord followed by a rest half beat 4 times, then the B minor seventh chord followed by a rest half beat 4 times, then the C major seventh chord breaking up the chord 1 time

```python
a = C('Am7') % (1/8, 0)
play(a * 4 | (a + 2) * 4 | get_chord(a[0] + 3, 'maj7').set(interval=1/8), bpm=80)
```

## A short piano piece

```python
a = C('Dmaj7') % (1/4,1/4) | C('Cmaj7') | C('Fadd9',3) | C('D#maj7',4) | (C('Dmaj7',3)/-2) % (5/4,)
b = chord('F#5, G5, A5, B5, G5', 1/8, 1/8)   
play(a & b, 140, instrument=1)
```

## chromatic downward alternating major seventh and minor seventh chords

```python
a = C('Amaj7') @ 2 * 4 | C('G#m7') @ 2 * 4 | C('Gmaj7') @ 2 * 4 | C('F#m7') @ 2 * 4    
play(a | a % (1/4, 1/4), 165, instrument=9)
```

## a piece of music with a scary atmosphere, orchestral sound

```python
a = (C('Bmaj9',3)/[2,3,4,1,5]) % (1/8,1/8)
b = (C('Bmaj9',3)/[2,3,4,1,5,2]) % (1/8, 1/8)
q = a + ~a[1:-1]
q2 = b + ~b[3:-1]
t = (q + q2) * 2
adding = chord(['Bb5','Ab5','Gb5','Ab5']) % (1/2,1/2) * 2
t2 = t & adding
play(t2 + (t2 - 3), 100, instrument=47)
```

## very nice 6451 chord configuration, harp tone

```python
q = scale('C4', 'major')
r = q%(6451, 0.5/4, 0.3/4, 5)
r = [i.omit(5).inversion_highest(3) for i in r]
play(r*2, bpm=80, instrument=47)
```

## Another great sounding 6451 chord configuration, harp tone

```python
q = scale('C4', 'major')
r = q%(6451, 0.5/4, 0.3/4, 5)
r = [i.omit(7).inversion_highest(2) for i in r]
play(r*2, bpm=80, instrument=47)
```

## scary and eerie soundtrack, instruments used: steel-string acoustic guitar and orchestra

```python
a = C('Baug9', 4) @ [2, 3, 4, 1.1, 5, 1.1, 4, 3] % (1/8,1/8)
b = C('BmM9', 4) @ [2, 3, 4, 1.1, 5, 2.1, 5, 1.1] % (1/8,1/8)
part1 = (a + b)*2
part2 = (C('Baug9',4, 1, 0) | C('BmM9',4, 1, 0)) * 2
part2.set_volume(80)
play(P([part1, part2], [26,49], 100, [0,0]))
```

## very nice 6451 chord configuration, electric piano sound

```python
q = scale('C4', 'major')
r = q%(64516458, 1/2, 0.3/4, 5)
r = [i.omit(7).inversion_highest(2) for i in r]
play(r*2, bpm=80, instrument=5)
```

## 80s hard rock or pop metal style, instruments used: piano, synthesizer tone, electric bass

```python
a = chord('C2, G1, C2, Ab1, Bb1, G1', [15/8,1/8,2,2,1.5,3/4], [15/8,1/8,2,2,1.5,3/4])
b = C('Cm', 5, 1/8) | 1/4 | C('Bb', 4, 1/8) | 1/4 | C('Ab', 4, 1/8) | 1/4 | C('Bb', 4, 1/2) | 3/8
b2 = C('Cm', 5, 1/8) | 1/4 | C('Bb', 4, 1/8) | 1/4 | C('Abmaj7', 4, 1/8) | 1/4 | C('Gsus', 4, 3/4) | 1/8
c = (b * 3) | b2
a2 = chord('C2',1/8,1/8)*32 + chord('Ab1',1/8,1/8)*16 + chord('Bb1',1/8,1/8)*12 + chord('G1',1/8,1/8)*4
play(piece([a, c, a2 * 2, c * 2], [1, 81, 34, 81], 130, [0, 1/4, 8, 33/4]))
```

## horror ambient music, orchestral tones

```python
a = get_chord('B4','maj9').sort([2,3,4,1,5])
b = get_chord('B4','maj9').sort([2,3,4,1,5,2])
q = a + a[1:-1].reverse_chord()
q2 = b + b[3:-1].reverse_chord()
play((q.set(1/8,1/8) + q2.set(1/8,1/8))*2, 100, instrument=50)
```

