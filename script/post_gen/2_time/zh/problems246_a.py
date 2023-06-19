Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    x3,y3 = map(int, input().split())
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    print('{} {}'.format(x4,y4))

=======
Suggestion 2

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    else:
        x = x1
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    else:
        y = y1
    print(x, y)

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    
    print(x4, y4)

=======
Suggestion 4

def get_coordinate(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    else:
        x = x1
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    else:
        y = y1
    return x, y

=======
Suggestion 5

def get_coordinate():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    else:
        x = x1
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    else:
        y = y1
    print(x, y)

get_coordinate()

=======
Suggestion 6

def getPoint(x1,y1,x2,y2,x3,y3):
    x4 = 0
    y4 = 0
    if x1==x2:
        x4 = x3
    elif x1==x3:
        x4 = x2
    else:
        x4 = x1

    if y1==y2:
        y4 = y3
    elif y1==y3:
        y4 = y2
    else:
        y4 = y1

    return x4,y4

=======
Suggestion 7

def get_vertex(x1, y1, x2, y2, x3, y3):
    x4 = x3 + x1 - x2
    y4 = y3 + y1 - y2
    return x4, y4

=======
Suggestion 8

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x4 = x3 - x2 + x1
    y4 = y3 - y2 + y1

    print(x4, y4)

=======
Suggestion 9

def find_point(x1,y1,x2,y2,x3,y3):
    if x1==x2:
        x4=x3
    elif x1==x3:
        x4=x2
    elif x2==x3:
        x4=x1
    if y1==y2:
        y4=y3
    elif y1==y3:
        y4=y2
    elif y2==y3:
        y4=y1
    return x4,y4
