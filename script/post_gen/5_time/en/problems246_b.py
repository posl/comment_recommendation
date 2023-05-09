Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print("{0:.10f} {1:.10f}".format((A-1)/(A+B-1), (B-1)/(A+B-1)))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(a/(a+b))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    x = b/a
    print(x)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A/(A+B))

=======
Suggestion 6

def solve():
    A, B = map(int, input().split())
    print(A / (A + B))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    #print(a, b)
    print(a / (a + b))

=======
Suggestion 8

def main():
    import sys
    import math

    input = sys.stdin.readline
    a, b = map(int, input().split())
    print(b/a)

=======
Suggestion 9

def get_input():
    a, b = input().split()
    return int(a), int(b)
