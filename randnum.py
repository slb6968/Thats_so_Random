#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides examples of how to use the Random and Calendar modules."""

import random
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

# Some examples of functions in the random module

listitems = [9, 23, 39485, -132, 0, -55]

ranflt = random.random()
ranint = random.randint(298, 7365)
ransamp = random.sample(listitems, 3)

print 'A random floating point number between 0.0 and 1.0 is: ', ranflt
print 'And here\'s a random integer between 298 and 7365: ', ranint
print 'Plus a random sampling of three items in a pre-defined list', \
      listitems, ':', ransamp

# Uses the randint function to display a calendar of a random month


def gencal():
    """Generates a set of random numbers, then displays a calendar for that
    date, which is between 1/1970 and 12/2016.

    Args:
        None

    Returns:
        Prints a formatted one-month calendar.

    Raises:
        ValueError: day is out of range for month
        This error is returned when dyz is greater than the number of days in
        calendar month moy. For example, dyz=31 & moy=6 OR dyz=30 & moy=2. 
    """
    yrx = random.randint(1970, 2016)
    moy = random.randint(1, 12)
    dyz = random.randint(1, 31)
    print '\n-  -  -  - Generating A Random Month\'s Calendar -  -  -  -\n'
    print moy, dyz, yrx, 'falls on Day', calendar.weekday(yrx, moy, dyz), 'of the week.'
    print '\n(Monday = Day 0, Tuesday = Day 1, Wednesday = Day 2, . . . )\n'
    print 'And here is the calendar for ', moy, yrx, ':\n'
    print calendar.month(yrx, moy)
    return
