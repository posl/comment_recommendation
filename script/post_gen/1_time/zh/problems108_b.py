Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems108_b():
    pass

=======
Suggestion 2

def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 + y1 - y2
    y3 = y2 + x2 - x1
    x4 = x1 + y1 - y2
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

=======
Suggestion 4

def main():
    x1,y1,x2,y2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = x1 - (y2 - y1)
    y3 = y1 - (x1 - x2)
    x4 = x2 - (y2 - y1)
    y4 = y2 - (x1 - x2)
    print(x3,y3,x4,y4)
    return

=======
Suggestion 5

def problems108_b(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = x2 - (y2 - y1), y2 + (x2 - x1), x1 - (y2 - y1), y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======
Suggestion 7

def problems108_b():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3 = x2-(y2-y1),y2+(x2-x1)
    x4,y4 = x1-(y2-y1),y1+(x2-x1)
    print(x3,y3,x4,y4)

=======
Suggestion 8

def problems108_b():
    x1,y1,x2,y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)
