Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y0 - y2) / 2
    y1 = (y0 + y2) / 2 + (x2 - x0) / 2
    print(x1, y1)

=======
Suggestion 2

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2
    y1 = (y0 + y2) / 2
    print(x1, y1)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y0 - y2) / (N / 2)
    y1 = (y0 + y2) / 2 + (x2 - x0) / (N / 2)
    print(x1, y1)

=======
Suggestion 4

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y0 - y2) / 2
    y1 = (y0 + y2) / 2 + (x2 - x0) / 2
    print(x1, y1)

=======
Suggestion 5

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    dx = (x1 - x0) / (N / 2)
    dy = (y1 - y0) / (N / 2)
    print(x1 - dy, y1 + dx)

=======
Suggestion 6

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    dx = (x1 - x0) / (N / 2)
    dy = (y1 - y0) / (N / 2)
    print(x1 + dx, y1 + dy)

=======
Suggestion 7

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = x0 + x2 - y0 + y2
    y1 = y0 + x2 - x0 + y2
    print(x1, y1)

=======
Suggestion 8

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = x0 + x1 - x0
    y2 = y0 + y1 - y0
    print(x2, y2)

=======
Suggestion 9

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1) / 2 + (y0 - y1) / (2 * n), (y0 + y1) / 2 + (x1 - x0) / (2 * n))
