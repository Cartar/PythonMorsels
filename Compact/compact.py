"""
For this week's exercise I want you to write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]
There are two bonuses for this exercise.

I recommend solving the exercise without the bonuses first and then attempting each bonus separately.

Bonus 1

For the first bonus, make sure you accept any iterable as an argument, not just a sequence (which means you can't use index look-ups in your answer). ✔️

Here's an example with a generator expression, which is a lazy iterable:

>>> compact(n**2 for n in [1, 2, 2])
[1, 4]
Bonus 2

As a second bonus, make sure you return an iterator from your compact function instead of a list. ✔️

>>> c = compact(n**2 for n in [1, 2, 2])
>>> iter(c) is c
True
This should allow your compact function to accept infinitely long iterables (or other lazy iterables).
"""

from itertools import groupby

def compact_generator(sequence):
    "Function to compact an input sequence"
    previous = object()
    for val in sequence:
        if val != previous:
            yield val
            previous = val

def compact(iterable):
    return (
        item
        for item, group in groupby(iterable)
    )
