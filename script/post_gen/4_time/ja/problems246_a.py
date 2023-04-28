Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
    # input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # compute
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

    # output
    print(x4, y4)

=======
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 != x2 and x1 != x3:
        x = x1
    elif x2 != x1 and x2 != x3:
        x = x2
    elif x3 != x1 and x3 != x2:
        x = x3

    if y1 != y2 and y1 != y3:
        y = y1
    elif y2 != y1 and y2 != y3:
        y = y2
    elif y3 != y1 and y3 != y2:
        y = y3

    print(x, y)
    return

=======
Suggestion 5

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4 = x1
    y4 = y1
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    print(str(x4) + " " + str(y4))

=======
Suggestion 6

def get_point(x1, y1, x2, y2, x3, y3):
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

    return x4, y4
