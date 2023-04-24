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
    x1,y1,x2,y2 = map(int,input().split())
    print(x2-(y2-y1),y2+(x2-x1),x1-(y2-y1),y1+(x2-x1))

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3 = x2 - (y2 - y1), y2 + (x2 - x1)
    x4, y4 = x1 - (y2 - y1), y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======
Suggestion 4

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======
Suggestion 5

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_3 = x_2 + (y_1 - y_2)
    y_3 = y_2 - (x_1 - x_2)
    x_4 = x_3 + (x_1 - x_2)
    y_4 = y_3 + (y_1 - y_2)
    print(x_3, y_3, x_4, y_4)

=======
Suggestion 6

def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x1 - (y2-y1)
    y3 = y1 + (x2-x1)
    x4 = x2 - (y2-y1)
    y4 = y2 + (x2-x1)
    print(x3,y3,x4,y4)

=======
Suggestion 7

def main():
	x1, y1, x2, y2 = map(int, input().split())
	x3 = x2 + y1 - y2
	y3 = y2 - x1 + x2
	x4 = x1 + y1 - y2
	y4 = y1 - x1 + x2
	print(x3, y3, x4, y4)
