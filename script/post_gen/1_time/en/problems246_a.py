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

main()

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4 = x3 + x2 - x1
    y4 = y3 + y2 - y1
    print(x4, y4)

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

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    print(x1 + x2 - x3, y1 + y2 - y3)

=======
Suggestion 6

def main():
    # Read all the input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Calculate the x coordinate of the fourth vertex
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    # Calculate the y coordinate of the fourth vertex
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    # Print the result
    print(x4, y4)
