Synthesizing 10/10 solutions

=======
Suggestion 1

def get_vertex(x1, y1, x2, y2, x3, y3):
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

    return x4, y4

=======
Suggestion 2

def get_coordinate():
    #get the coordinate of the point
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    #get the coordinate of the forth point
    x4 = x2 + x3 - x1
    y4 = y2 + y3 - y1
    print(x4,y4)

=======
Suggestion 3

def problems246_a():
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

=======
Suggestion 4

def problem246_a():
    x_1 = int(input('x_1:'))
    y_1 = int(input('y_1:'))
    x_2 = int(input('x_2:'))
    y_2 = int(input('y_2:'))
    x_3 = int(input('x_3:'))
    y_3 = int(input('y_3:'))
    if x_1 == x_2:
        x_4 = x_3
    elif x_1 == x_3:
        x_4 = x_2
    else:
        x_4 = x_1
    if y_1 == y_2:
        y_4 = y_3
    elif y_1 == y_3:
        y_4 = y_2
    else:
        y_4 = y_1
    print(x_4,y_4)

=======
Suggestion 5

def get_point(x1,y1,x2,y2,x3,y3):
    x = 0
    y = 0
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
    return x,y

=======
Suggestion 6

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
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
    print(x4,y4)

=======
Suggestion 7

def getTheFourthPoint():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
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
getTheFourthPoint()

=======
Suggestion 8

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
Suggestion 9

def get_coordinate():
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

    print(x4,y4)

get_coordinate()

=======
Suggestion 10

def get_point(x1,y1,x2,y2,x3,y3):
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
