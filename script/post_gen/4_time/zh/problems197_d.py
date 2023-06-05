Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems197_d():
    pass

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    x2 = (x0 + x1 + (y1 - y0) * (2 / 3) ** 0.5) / 2
    y2 = (y0 + y1 + (x0 - x1) * (2 / 3) ** 0.5) / 2
    print(x2, y2)

=======
Suggestion 4

def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = (x0 + x2 + (y2 - y0) * (3 ** 0.5)) / 2
    y1 = (y0 + y2 + (x0 - x2) * (3 ** 0.5)) / 2

    print('{0:.11f} {1:.11f}'.format(x1, y1))
