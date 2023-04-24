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
    x1 = (x0 + x2) / 2 - (y2 - y0) / 2
    y1 = (y0 + y2) / 2 + (x2 - x0) / 2
    print(x1, y1)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = (x0 + x2) / 2
    y1 = (y0 + y2) / 2

    print(x1, y1)

=======
Suggestion 4

def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    x_1 = (x_0 + x_N_2) / 2 - (y_0 - y_N_2) / (N / 2)
    y_1 = (y_0 + y_N_2) / 2 + (x_0 - x_N_2) / (N / 2)
    print(x_1, y_1)

main()

=======
Suggestion 5

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = x1 + x1 - x0
    y2 = y1 + y1 - y0
    print(x2, y2)

=======
Suggestion 6

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x = (x0 + x1) / 2
    y = (y0 + y1) / 2
    x2 = (x0 - x1) / (N - 4) + x
    y2 = (y0 - y1) / (N - 4) + y
    print(x2, y2)

=======
Suggestion 7

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1) / 2 + (y0 - y1) * (N / 4) / (N / 2), (y0 + y1) / 2 + (x1 - x0) * (N / 4) / (N / 2))

=======
Suggestion 8

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x1 - x0) * (n / 4) + x0, (y1 - y0) * (n / 4) + y0)

=======
Suggestion 9

def main():
    N = int(input())
    x0, y0 = map(float, input().split())
    x1, y1 = map(float, input().split())
    x2 = x1 + (x1 - x0)
    y2 = y1 + (y1 - y0)
    print(x2, y2)

=======
Suggestion 10

def main():
    N = int(input())
    x0,y0 = map(int,input().split())
    x1,y1 = map(int,input().split())
    x2 = x1 + (x1-x0)
    y2 = y1 + (y1-y0)
    print(x2,y2)
