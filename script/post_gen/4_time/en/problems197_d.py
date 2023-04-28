Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    # compute

    # output
    print(xN2 + (x0 - xN2) * (2 ** 0.5))
    print(yN2 + (y0 - yN2) * (2 ** 0.5))

=======
Suggestion 2

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2 + (yN2 - y0) * 3**0.5) / 2
    y1 = (y0 + yN2 + (x0 - xN2) * 3**0.5) / 2
    print(x1, y1)

=======
Suggestion 3

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + (y0 - y2) * (2 ** 0.5)) / 2
    y1 = (y0 + y2 + (x2 - x0) * (2 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 4

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())
    x1 = (x0 + xn2 + (y0 - yn2) * (3 ** 0.5)) / 2
    y1 = (y0 + yn2 + (xn2 - x0) * (3 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 5

def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2

    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2

    theta = 2 * math.pi / N
    x3 = x2 * math.cos(theta) - y2 * math.sin(theta)
    y3 = x2 * math.sin(theta) + y2 * math.cos(theta)

    x1 = x1 + x3
    y1 = y1 + y3

    print(x1, y1)

=======
Suggestion 6

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    x2 = (x0 + x1 + (y1 - y0) * (2 ** 0.5)) / 2
    y2 = (y0 + y1 - (x1 - x0) * (2 ** 0.5)) / 2

    print(x2, y2)

=======
Suggestion 7

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0+x1)/2
    y2 = (y0+y1)/2
    x3 = x0 - (y0-y2)
    y3 = y0 + (x0-x2)
    print(x3, y3)

=======
Suggestion 8

def solve():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + (y0 - y2) * (2 ** 0.5)) / 2
    y1 = (y0 + y2 + (x2 - x0) * (2 ** 0.5)) / 2
    print('{:.10f} {:.10f}'.format(x1, y1))

=======
Suggestion 9

def solve(n, x0, y0, x2, y2):
    return (x0+x2+(y0-y2)*((3**0.5)/3), y0+y2+(x2-x0)*((3**0.5)/3))

=======
Suggestion 10

def problems197_d():
    return 0
