Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

    print("{} {}".format(x4, y4))

=======
Suggestion 3

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
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2:
        x4 = x3
    elif x2 == x3:
        x4 = x1
    elif x3 == x1:
        x4 = x2

    if y1 == y2:
        y4 = y3
    elif y2 == y3:
        y4 = y1
    elif y3 == y1:
        y4 = y2

    print(x4, y4)

=======
Suggestion 5

def solve():
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
Suggestion 6

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
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
Suggestion 7

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
Suggestion 8

def main():
    # 標準入力の受け取り
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # 計算
    x4 = 0
    y4 = 0
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

    # 結果の出力
    print(x4, y4)

=======
Suggestion 9

def getPoint(p1, p2, p3):
    if p1[0] == p2[0]:
        x = p3[0]
    elif p1[0] == p3[0]:
        x = p2[0]
    else:
        x = p1[0]
    if p1[1] == p2[1]:
        y = p3[1]
    elif p1[1] == p3[1]:
        y = p2[1]
    else:
        y = p1[1]
    return x, y
