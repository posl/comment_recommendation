Synthesizing 10/10 solutions

=======
Suggestion 1

def problem246_a():
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
Suggestion 2

def find_another_point(x1, y1, x2, y2, x3, y3):
    x4 = 0
    y4 = 0
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
Suggestion 3

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
    print(x4, y4)

=======
Suggestion 4

def get_point(x, y):
    for i in range(3):
        if x[i] == x[i-1]:
            x.append(x[i-2])
        elif x[i] == x[i-2]:
            x.append(x[i-1])
        else:
            x.append(x[i])
    for i in range(3):
        if y[i] == y[i-1]:
            y.append(y[i-2])
        elif y[i] == y[i-2]:
            y.append(y[i-1])
        else:
            y.append(y[i])
    return x[-1], y[-1]

=======
Suggestion 5

def main():
    x = []
    y = []
    for i in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(3):
        if x.count(x[i]) == 1:
            x4 = x[i]
        if y.count(y[i]) == 1:
            y4 = y[i]
    print(x4, y4)

=======
Suggestion 6

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4 = x3 + x1 - x2
    y4 = y3 + y1 - y2
    print(x4,y4)

=======
Suggestion 7

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4 = x3 + (x2 - x1)
    y4 = y3 + (y2 - y1)
    print(x4,y4)

=======
Suggestion 8

def find_point():
    point1 = input().split()
    point2 = input().split()
    point3 = input().split()
    x1,y1 = int(point1[0]),int(point1[1])
    x2,y2 = int(point2[0]),int(point2[1])
    x3,y3 = int(point3[0]),int(point3[1])
    x4,y4 = 0,0
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
    print(x4,y4)

=======
Suggestion 9

def get_point():
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if x1==x2:
        x4=x3
    elif x1==x3:
        x4=x2
    else:
        x4=x1
    if y1==y2:
        y4=y3
    elif y1==y3:
        y4=y2
    else:
        y4=y1
    print(x4,y4)

get_point()

=======
Suggestion 10

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    elif x2 == x3:
        x = x1

    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    elif y2 == y3:
        y = y1

    print('{} {}'.format(x, y))
