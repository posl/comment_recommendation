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
    elif x2 == x3:
        x = x1
    elif x3 == x1:
        x = x2
    if y1 == y2:
        y = y3
    elif y2 == y3:
        y = y1
    elif y3 == y1:
        y = y2
    print(x, y)

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x4 = x1 + x2 - x3
    y4 = y1 + y2 - y3

    print(x4, y4)

=======
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4 = x1 + x3 - x2
    y4 = y1 + y3 - y2
    print(x4, y4)

=======
Suggestion 5

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    print((x1 + x2 + x3) - (x1 + x2 + x3) // 3, (y1 + y2 + y3) - (y1 + y2 + y3) // 3)

=======
Suggestion 6

def main():
    # x1, y1, x2, y2, x3, y3 = map(int, input().split())
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
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
Suggestion 7

def main():
    x = []
    y = []
    for i in range(3):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    for i in range(3):
        if x.count(x[i]) == 1:
            print(x[i], end=" ")
        if y.count(y[i]) == 1:
            print(y[i])
