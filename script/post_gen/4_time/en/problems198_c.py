Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**(1/2)
    if d < R:
        print(2)
    else:
        print(int(d//R + 1) if d%R != 0 else int(d//R))
    return 0

=======
Suggestion 2

def main():
    import math
    R, X, Y = map(int, input().split())
    distance = math.sqrt(X**2 + Y**2)
    if distance % R == 0:
        print(int(distance / R))
    else:
        print(math.ceil(distance / R))

=======
Suggestion 3

def main():
    r,x,y = map(int,input().split())
    d = (x**2 + y**2)**(1/2)
    if d == r:
        print(1)
    elif d <= 2*r:
        print(2)
    else:
        print(int(d/r))

=======
Suggestion 4

def solve():
    R,X,Y = map(int,input().split())
    if (X**2+Y**2)**0.5 == R:
        print(1)
    elif (X**2+Y**2)**0.5 < R:
        print(2)
    else:
        print(int((X**2+Y**2)**0.5//R)+1)

=======
Suggestion 5

def main():
    R, X, Y = map(int, input().split())
    import math
    if (X**2 + Y**2) % R**2 == 0:
        print(int(math.sqrt(X**2 + Y**2) // R))
    else:
        print(int(math.sqrt(X**2 + Y**2) // R + 1))

=======
Suggestion 6

def solve():
    #import sys
    #input = sys.stdin.readline
    R, X, Y = map(int, input().split())
    import math
    d = math.sqrt(X*X + Y*Y)
    if d < R:
        return 2
    else:
        return math.ceil(d/R)

print(solve())

=======
Suggestion 7

def solve():
    R,X,Y = map(int,input().split())
    import math
    d = math.sqrt(X*X+Y*Y)
    if d < R:
        return 2
    else:
        return math.ceil(d/R)

print(solve())

=======
Suggestion 8

def main():
    # input
    R, X, Y = map(int, input().split())

    # compute

    # output
    if R*R > X*X + Y*Y:
        print(2)
    elif (R*R == X*X + Y*Y) or ((R*R - (X*X + Y*Y)) % (2*R) == 0):
        print((R*R - (X*X + Y*Y)) // (2*R) + 1)
    else:
        print((R*R - (X*X + Y*Y)) // (2*R) + 2)

=======
Suggestion 9

def solve(r, x, y):
    from math import sqrt
    d = sqrt(x**2 + y**2)
    if d < r:
        return 2
    return int(d/r)+1

=======
Suggestion 10

def main():
    import sys
    import math
    import re

    def get_list():
        return list(map(int, sys.stdin.readline().strip().split()))

    def get_int():
        return int(sys.stdin.readline().strip())

    def get_str():
        return sys.stdin.readline().strip()

    def get_list_str():
        return list(sys.stdin.readline().strip())

    R, X, Y = get_list()

    if (X**2 + Y**2)**(1/2) < R:
        print(2)
    else:
        print(math.ceil((X**2 + Y**2)**(1/2)/R))
