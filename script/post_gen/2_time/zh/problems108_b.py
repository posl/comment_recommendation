Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems108_b():
    pass

=======
Suggestion 2

def main():
    x1,y1,x2,y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)

=======
Suggestion 3

def main():
    x1,y1,x2,y2 = map(int,input().split())
    print(x2+y1-y2,y2+x2-x1,x1+y1-y2,y1+x2-x1)

=======
Suggestion 4

def p108_b():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3,y3,x4,y4)

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

=======
Suggestion 6

def main():
    x1,y1,x2,y2 = [int(i) for i in input().strip().split()]
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3,y3,x4,y4)

=======
Suggestion 7

def get4thPoint(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    return x3,y3,x4,y4

=======
Suggestion 8

def problems108_b():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)
