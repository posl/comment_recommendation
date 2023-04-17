Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 + y1 - y2
    y3 = y2 + x2 - x1
    x4 = x3 + x2 - x1
    y4 = y3 + y2 - y1
    print(x3, y3, x4, y4)

=======

def main():
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x3 - (x2 - x1)
    y4 = y3 - (y2 - y1)
    print(x3, y3, x4, y4)

=======

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_3 = x_2 - y_2 + y_1
    y_3 = y_2 + x_2 - x_1
    x_4 = x_3 - (y_3 - y_1)
    y_4 = y_3 - (x_3 - x_1)
    print(x_3, y_3, x_4, y_4)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        x3 = x1 + abs(y2 - y1)
        x4 = x2 + abs(y2 - y1)
        y3 = y1
        y4 = y2
    elif y1 == y2:
        y3 = y1 + abs(x2 - x1)
        y4 = y2 + abs(x2 - x1)
        x3 = x1
        x4 = x2
    else:
        x3 = x2
        y3 = y1
        x4 = x1
        y4 = y2
    print(x3, y3, x4, y4)
