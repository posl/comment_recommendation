Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2

    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2

    import math
    x3 = x2 * math.cos(2 * math.pi / N) - y2 * math.sin(2 * math.pi / N)
    y3 = x2 * math.sin(2 * math.pi / N) + y2 * math.cos(2 * math.pi / N)

    print(x3 + x1, y3 + y1)

=======
Suggestion 2

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())

    x1 = (x0 + xn2) / 2
    y1 = (y0 + yn2) / 2

    radian = 2 * math.pi / n
    x2 = (x0 - x1) * math.cos(radian) - (y0 - y1) * math.sin(radian) + x1
    y2 = (x0 - x1) * math.sin(radian) + (y0 - y1) * math.cos(radian) + y1

    print("{:.11f} {:.11f}".format(x2, y2))

=======
Suggestion 3

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + (y2 - y0) * (2 ** 0.5)) / 2
    y1 = (y0 + y2 + (x0 - x2) * (2 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 4

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2

    # rotate
    x3 = x0 - x2
    y3 = y0 - y2

    x4 = -y3
    y4 = x3

    # translate
    x5 = x4 + x2
    y5 = y4 + y2

    print(x5, y5)

=======
Suggestion 5

def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y0 - y2) * (3 ** 0.5) / 2
    y1 = (y0 + y2) / 2 + (x2 - x0) * (3 ** 0.5) / 2
    print(x1, y1)

=======
Suggestion 6

def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2 + (y0 - yN2) * (3 ** 0.5)) / 2
    y1 = (y0 + yN2 + (xN2 - x0) * (3 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 7

def solve():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + (y2 - y0) * (2 ** 0.5)) / 2
    y1 = (y0 + y2 + (x0 - x2) * (2 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 8

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = (x0 + x2 + ((y2 - y0) * 3**0.5)) / 2
    y1 = (y0 + y2 + ((x0 - x2) * 3**0.5)) / 2
    print(x1, y1)

=======
Suggestion 9

def main():
    N = int(input())
    N2 = int(N/2)
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    x1 = (x0 + xN2 + (yN2 - y0) * (2 ** 0.5)) / 2
    y1 = (y0 + yN2 + (x0 - xN2) * (2 ** 0.5)) / 2

    print(x1, y1)

=======
Suggestion 10

def solve(n, x0, y0, x1, y1):
    x2 = (x0 + x1 + (y0 - y1) * (3 ** 0.5)) / 2
    y2 = (y0 + y1 + (x1 - x0) * (3 ** 0.5)) / 2
    return x2, y2
