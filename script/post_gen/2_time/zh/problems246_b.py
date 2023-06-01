Synthesizing 10/10 solutions

=======
Suggestion 1

def get_coordinate(x1, y1, x2, y2, x3, y3):
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
    return x4, y4

=======
Suggestion 2

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    print(x1 + x3 - x2, y1 + y3 - y2)

=======
Suggestion 3

def solve():
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

solve()

=======
Suggestion 4

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
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
    print(x4,y4)

=======
Suggestion 5

def solve():
    # 读取输入
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # 由于矩形的边与x轴或y轴平行，所以可以分别求出矩形的水平边和垂直边
    # 水平边的长度为x1-x2，垂直边的长度为y1-y2
    # 由于矩形的面积不为0，所以水平边和垂直边的长度不可能同时为0
    # 所以可以根据水平边和垂直边的长度来判断矩形的另外两个点的坐标
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

    # 输出结果
    print(x4, y4)

=======
Suggestion 6

def find_point(x1,y1,x2,y2,x3,y3):
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

    return x4,y4

=======
Suggestion 7

def main():
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    x3,y3 = map(int, input().split())
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

    print(str(x4) + " " + str(y4))

=======
Suggestion 8

def getPoint(x1,y1,x2,y2,x3,y3):
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

    return x,y

=======
Suggestion 9

def get_point():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x4 = x1 + x2 + x3 - min(x1, x2, x3) - max(x1, x2, x3)
    y4 = y1 + y2 + y3 - min(y1, y2, y3) - max(y1, y2, y3)

    print(x4, y4)

=======
Suggestion 10

def get_point(x1,y1,x2,y2,x3,y3):
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
    return x4,y4
