Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    dx = x1 - x0
    dy = y1 - y0
    x2 = x1 - dy
    y2 = y1 + dx
    print(x2, y2)

=======
Suggestion 2

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2.0
    y1 = (y0 + y2) / 2.0
    print(x1, y1)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2 + (y1 - y0) / (2 * N)
    y2 = (y0 + y1) / 2 - (x1 - x0) / (2 * N)
    print(x2, y2)

=======
Suggestion 4

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) - y0 + y2
    y1 = (y0 + y2) - x2 + x0
    print(x1, y1)

=======
Suggestion 5

def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    print((x_0 + x_N_2) / 2, (y_0 + y_N_2) / 2)

=======
Suggestion 6

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = (x0 + x1) / 2, (y0 + y1) / 2
    x3 = x2 - (y2 - y0)
    y3 = y2 + (x2 - x0)
    print(x3, y3)

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 8

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    x1 = (N/2*x0+xN2)/(N/2+1)
    y1 = (N/2*y0+yN2)/(N/2+1)
    print(x1, y1)

=======
Suggestion 9

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    x1 = (x0 + x2) / 2
    y1 = (y0 + y2) / 2
    print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2
    # y1 = (y0 + y2) / 2
    # print(x1, y1)
    # x1 = (x0 + x2) / 2

=======
Suggestion 10

def Main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = xN2 + (xN2 - x0) * (N / 4) / (N / 2)
    y1 = yN2 + (yN2 - y0) * (N / 4) / (N / 2)
    print(x1, y1)
