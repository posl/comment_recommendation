Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

    print('{} {}'.format(x4, y4))

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

def problem246_a():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2:
        print(x3, y3)
    elif x1 == x3:
        print(x2, y2)
    elif x2 == x3:
        print(x1, y1)

=======
Suggestion 5

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4 = x3 + x1 - x2
    y4 = y3 + y1 - y2
    print(x4, y4)

=======
Suggestion 6

def main():
    # Take input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Calculate the fourth vertex
    x4 = x3 - (y2 - y1)
    y4 = y3 + (x2 - x1)

    # Print the output
    print(x4, y4)

=======
Suggestion 7

def main():
    # Read from Standard Input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Solve the problem
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

    # Write to Standard Output
    print('{} {}'.format(x4, y4))

=======
Suggestion 8

def solve():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
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
    print(x,y)

=======
Suggestion 9

def get_other_vertex(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        if y1 == y3:
            return x3, y2
        else:
            return x3, y1
    elif x1 == x3:
        if y1 == y2:
            return x2, y3
        else:
            return x2, y1
    else:
        if y1 == y2:
            return x1, y3
        else:
            return x1, y2
