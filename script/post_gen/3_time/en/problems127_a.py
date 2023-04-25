Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(0)

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A < 6:
        print("0")
    elif A >= 6 and A <= 12:
        print(str(B//2))
    else:
        print(str(B))

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b//2)
    else:
        print(0)
    return

=======
Suggestion 7

def main():
    age, cost = map(int, input().split())
    if age < 6:
        print(0)
    elif age < 13:
        print(cost // 2)
    else:
        print(cost)

main()

I think it's a good idea to use the input() function with the map() function to convert the input into the desired type.

=======
Suggestion 8

def main():
    #input
    A,B = map(int, input().split())
    #output
    if A>=13:
        print(B)
    elif A>=6:
        print(B//2)
    else:
        print(0)

=======
Suggestion 9

def main():
    #input
    a,b = map(int, input().split())

    #output
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)

main()

Python 3.4.3 (default, Nov 17 2016, 01:08:31) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version
'3.4.3 (default, Nov 17 2016, 01:08:31) [GCC]'
>>> sys.version_info
sys.version_info(major=3, minor=4, micro=3, releaselevel='final', serial=0)
>>>

import sys
print(sys.version)
print(sys.version_info)
