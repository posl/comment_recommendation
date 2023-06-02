Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 + y1 - y2
    y3 = y2 + x2 - x1
    x4 = x1 + y1 - y2
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

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

def get_x3_y3_x4_y4(x1,y1,x2,y2):
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x3 - x2 + x1
    y4 = y3 - y2 + y1
    return x3,y3,x4,y4

=======
Suggestion 4

def find4points(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    return x3,y3,x4,y4

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 - (x1 - x2)
    x4 = x1 - (y2 - y1)
    y4 = y1 - (x1 - x2)
    print(x3, y3, x4, y4)

=======
Suggestion 6

def solve():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)
