Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 3

def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                print(a, b)
                return
    print(0, 0)

=======
Suggestion 4

def main():
    X = int(input())
    for A in range(-120,120):
        for B in range(-120,120):
            if A**5 - B**5 == X:
                print(A,B)
                return

=======
Suggestion 5

def main():
    X = int(input())
    for i in range(-118, 120):
        for j in range(-119, 119):
            if i**5 - j**5 == X:
                print(i, j)
                return

=======
Suggestion 6

def solve():
    X = int(input())
    for A in range(-1000, 1000):
        for B in range(-1000, 1000):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 7

def main():
    x = int(input())
    a = 0
    b = 0
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
    print(a,b)

=======
Suggestion 8

def problem166_d():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == x:
                print(a, b)
                exit()

=======
Suggestion 9

def solve(X):
    for A in range(-1000, 1000):
        for B in range(-1000, 1000):
            if A**5 - B**5 == X:
                return A, B

=======
Suggestion 10

def main():
    import sys
    import math

    x = int(input())

    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if a**5-b**5 == x:
                print(a, b)
                sys.exit()
