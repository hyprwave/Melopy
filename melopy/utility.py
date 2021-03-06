def frequency_from_key(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)

def frequency_from_note(note):
    """Returns the frequency of a note represented by a string"""
    return frequency_from_key(key_from_note(note))

def key_from_note(note):
    """Returns the key number (keys from A0) from a note represented by a string"""
    indices = { 'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11 }

    octave = 4

    if note[-1] in '012345678':
        octave = int(note[-1])

    tone = indices[note[0].upper()]
    key = 12 * octave + tone

    if len(note) > 1 and note[1] == '#':
        key += 1
    elif len(note) > 1 and note[1] == 'b':
        key -= 1

    return key - 8;

def note_from_key(key):
    """Returns a string representing a note which is (key) keys from A0"""
    notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
    octave = (key + 8) / 12
    note = notes[(key -1 ) % 12]

    return note.upper() + str(octave)

# Licensed under The MIT License (MIT)
# See LICENSE file for more