Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 - (y2 - y0) / (2 * N)
    y1 = (y0 + y2) / 2 + (x2 - x0) / (2 * N)
    print(x1, y1)

=======
Suggestion 2

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y2 - y0) / (2 * N)
    y1 = (y0 + y2) / 2 + (x0 - x2) / (2 * N)
    print(x1, y1)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    dx = x2 - x0
    dy = y2 - y0
    x1 = x0 - dx
    y1 = y0 - dy

    print(x1, y1)

=======
Suggestion 4

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = 2 * x2 - x0
    y1 = 2 * y2 - y0
    print(x1, y1)

=======
Suggestion 5

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = (x0 + x2) / 2 - (y2 - y0) / (2 * N) * (N - 2)
    y1 = (y0 + y2) / 2 + (x2 - x0) / (2 * N) * (N - 2)

    print(x1, y1)

=======
Suggestion 6

def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N2, y_N2 = map(int, input().split())
    x_1 = (x_0 + x_N2) / 2 + (y_0 - y_N2) * (N / 4)**0.5
    y_1 = (y_0 + y_N2) / 2 + (x_N2 - x_0) * (N / 4)**0.5
    print(x_1, y_1)

=======
Suggestion 7

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = ((n - 2) * x0 + 2 * x1) / (n + 2)
    y2 = ((n - 2) * y0 + 2 * y1) / (n + 2)
    print(x2, y2)

=======
Suggestion 8

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2)/2 - ((y0 - yN2)/2)/tan(radians(180/n))
    y1 = (y0 + yN2)/2 + ((x0 - xN2)/2)/tan(radians(180/n))
    print(x1, y1)

=======
Suggestion 9

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1 + (y0 - y1) * (N / 4)) / 2, (y0 + y1 + (x1 - x0) * (N / 4)) / 2)

=======
Suggestion 10

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    # x1, y1を求める
    x1 = (x0 + x2) / 2 - (y2 - y0) / (2 * math.tan(math.pi / N))
    y1 = (y0 + y2) / 2 + (x2 - x0) / (2 * math.tan(math.pi / N))
    print(x1, y1)
