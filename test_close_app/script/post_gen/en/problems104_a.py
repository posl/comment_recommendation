Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    R = int(input())
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")

=======

def main():
    R = int(input())
    if R < 1200:
        print('ABC')
    elif R < 2800:
        print('ARC')
    else:
        print('AGC')

=======

def get_next_contest(rating):
    if rating < 1200:
        return "ABC"
    elif rating < 2800:
        return "ARC"
    else:
        return "AGC"

=======

def main():
    user_input = int(input())
    if user_input < 1200:
        print("ABC")
    elif user_input < 2800:
        print("ARC")
    else:
        print("AGC")

=======

def main():
    #input
    R = int(input())

    #output
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")

=======

def findContest(rating):
    if rating < 1200:
        return "ABC"
    elif rating < 2800:
        return "ARC"
    else:
        return "AGC"

rating = int(input())
print(findContest(rating))

Python 3.6.5 (default, Apr 1 2018, 05:46:30) [GCC] on linux

Copyright (c) 1991-2017 Python Software Foundation; All Rights Reserved

>>> def findContest(rating):
...     if rating < 1200:
...         return "ABC"
...     elif rating < 2800:
...         return "ARC"
...     else:
...         return "AGC"
...
>>> rating = int(input())
1200
>>> print(findContest(rating))
ARC
>>>
