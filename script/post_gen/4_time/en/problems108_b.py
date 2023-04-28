Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x1 - y2 + y1
    y4 = y1 + x2 - x1
    print(x3, y3, x4, y4)

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    print(x2 - y2 + y1, y2 + x2 - x1, x1 - y2 + y1, y1 + x2 - x1)

=======
Suggestion 4

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_3 = x_2 + y_1 - y_2
    y_3 = y_2 + x_2 - x_1
    x_4 = x_1 + y_1 - y_2
    y_4 = y_1 + x_2 - x_1
    print(x_3, y_3, x_4, y_4)

=======
Suggestion 5

def solve(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    return [x3, y3, x4, y4]

=======
Suggestion 6

def problem108_b():
    x1, y1, x2, y2 = map(int, input().split())
    print(x2 - (y2 - y1), y2 + (x2 - x1), x1 - (y2 - y1), y1 + (x2 - x1))
