Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y0 - y2) / N
    y1 = (y0 + y2) / 2 + (x2 - x0) / N
    print(x1, y1)

=======
Suggestion 2

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 - (y2 - y0) / (N / 2)
    y1 = (y0 + y2) / 2 + (x2 - x0) / (N / 2)
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
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = (x0 + x2) / 2 - (y2 - y0) / 2
    y1 = (y0 + y2) / 2 + (x2 - x0) / 2

    print(x1, y1)

=======
Suggestion 5

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = x2 - x0
    y1 = y2 - y0

    print(x1, y1)

=======
Suggestion 6

def readinput():
    n=int(input())
    x0,y0=map(int,input().split())
    x2,y2=map(int,input().split())
    return n,x0,y0,x2,y2

=======
Suggestion 7

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2 + (y0 - y1) / 2
    y2 = (y0 + y1) / 2 + (x1 - x0) / 2
    print(x2, y2)

=======
Suggestion 8

def main():
    import sys
    import math
    input = sys.stdin.readline
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2
    y1 = (y0 + y2) / 2
    print(x1, y1)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    #処理
    x_1 = x_0 + (x_N_2 - x_0) * (N / 4) / (N / 2)
    y_1 = y_0 + (y_N_2 - y_0) * (N / 4) / (N / 2)
    #出力
    print(x_1, y_1)

=======
Suggestion 10

def main():
    N = int(input()) 
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x2 + 2 * x0) / 3
    y1 = (y2 + 2 * y0) / 3
    print(x1, y1)
