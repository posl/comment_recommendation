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
        x4 = x3
    elif x2 == x3:
        x4 = x1
    else:
        x4 = x2

    if y1 == y2:
        y4 = y3
    elif y2 == y3:
        y4 = y1
    else:
        y4 = y2

    print(x4, y4)

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x = x3
    elif x2 == x3:
        x = x1
    else:
        x = x2
    if y1 == y2:
        y = y3
    elif y2 == y3:
        y = y1
    else:
        y = y2
    print(x, y)

=======
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4 = x2 + x3 - x1
    y4 = y2 + y3 - y1
    print(x4, y4)

=======
Suggestion 5

def solve():
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
Suggestion 6

def main():
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    x3,y3 = map(int, input().split())
    x4 = x1 + x2 - x3
    y4 = y1 + y2 - y3
    print(x4, y4)

=======
Suggestion 7

def problem246_a():
    # Get input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Solve
    if x1 == x2:
        x4 = x3
    elif x2 == x3:
        x4 = x1
    else:
        x4 = x2

    if y1 == y2:
        y4 = y3
    elif y2 == y3:
        y4 = y1
    else:
        y4 = y2

    # Output
    print(x4, y4)

=======
Suggestion 8

def find_other_vertex():
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

find_other_vertex()

=======
Suggestion 9

def findMissingPoint(x1,y1,x2,y2,x3,y3):
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    elif x2 == x3:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    elif y2 == y3:
        y4 = y1
    return x4,y4

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = findMissingPoint(x1,y1,x2,y2,x3,y3)
print(x4,y4)
