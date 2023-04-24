Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print(x3, y3, x4, y4)

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    print(x2 - dy, y2 + dx, x1 - dy, y1 + dx)

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())

    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x3 - (x2 - x1)
    y4 = y3 - (y2 - y1)

    print(x3, y3, x4, y4)

=======
Suggestion 6

def main():
    x1,y1,x2,y2=map(int,input().split())
    x3=x2-y2+y1
    y3=y2+x2-x1
    x4=x1-y2+y1
    y4=y1+x2-x1
    print(x3,y3,x4,y4)
main()

=======
Suggestion 7

def main():
    x1,y1,x2,y2 = map(int,input().split())
    print(x2 - (y2 - y1), y2 + (x2 - x1), x1 - (y2 - y1), y1 + (x2 - x1))
