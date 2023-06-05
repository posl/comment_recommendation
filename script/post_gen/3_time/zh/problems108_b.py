Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems108_b():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3 = x2-y2+y1,x2-x1+y2
    x4,y4 = x1-y2+y1,x2-x1+y1
    print(x3,y3,x4,y4)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3,y3,x4,y4)

=======
Suggestion 4

def problems108_b(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    return x3,y3,x4,y4

=======
Suggestion 5

def getxy(x1,y1,x2,y2):
    x3 = x1+y1-y2
    y3 = y1-x1+x2
    x4 = x2+y1-y2
    y4 = y2-x1+x2
    return x3,y3,x4,y4

=======
Suggestion 6

def problems108_b():
    pass

=======
Suggestion 7

def main():
    x1,y1,x2,y2 = map(int,input().split())
    print(x2+y1-y2,y2+x2-x1,x1+y1-y2,y1+x2-x1)
    return 0

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = x2 - y2 + y1, y2 + x2 - x1, x1 - y2 + y1, y1 + x2 - x1
    print(x3, y3, x4, y4)

=======
Suggestion 9

def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = 0,0,0,0
    if x1 == x2:
        if y2 > y1:
            x3,y3 = x1 + (y2 - y1),y1 + (x1 - x2)
            x4,y4 = x2 + (y2 - y1),y2 + (x1 - x2)
        else:
            x3,y3 = x1 + (y1 - y2),y1 + (x1 - x2)
            x4,y4 = x2 + (y1 - y2),y2 + (x1 - x2)
    elif y1 == y2:
        if x2 > x1:
            x3,y3 = x1 + (y1 - y2),y1 + (x2 - x1)
            x4,y4 = x2 + (y1 - y2),y2 + (x2 - x1)
        else:
            x3,y3 = x1 + (y1 - y2),y1 + (x1 - x2)
            x4,y4 = x2 + (y1 - y2),y2 + (x1 - x2)
    else:
        x3,y3 = x1 + (y1 - y2),y1 + (x2 - x1)
        x4,y4 = x2 + (y1 - y2),y2 + (x2 - x1)
    print(x3,y3,x4,y4)
