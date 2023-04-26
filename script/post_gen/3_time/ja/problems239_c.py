Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    x3 = x2 - y
    y3 = y2 + x
    x4 = x3 - x
    y4 = y3 - y
    print("Yes" if x3 == x1 and y3 == y1 and x4 == x2 and y4 == y2 else "No")

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - x1
    y3 = y2 - y1
    x4 = -y3
    y4 = x3
    x5 = x4 + x1
    y5 = y4 + y1
    x6 = x5 + x2
    y6 = y5 + y2
    print(x5, y5, x6, y6)

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3 = x2 - x1, y2 - y1
    x4, y4 = x3 - y3, y3 + x3
    x5, y5 = x4 + x3, y4 + y3
    x6, y6 = x5 + x4, y5 + y4
    x7, y7 = x6 + x5, y6 + y5
    x8, y8 = x7 + x6, y7 + y6
    x9, y9 = x8 + x7, y8 + y7
    x10, y10 = x9 + x8, y9 + y8
    x11, y11 = x10 + x9, y10 + y9
    x12, y12 = x11 + x10, y11 + y10
    x13, y13 = x12 + x11, y12 + y11
    x14, y14 = x13 + x12, y13 + y12
    x15, y15 = x14 + x13, y14 + y13
    x16, y16 = x15 + x14, y15 + y14
    x17, y17 = x16 + x15, y16 + y15
    x18, y18 = x17 + x16, y17 + y16
    x19, y19 = x18 + x17, y18 + y17
    x20, y20 = x19 + x18, y19 + y18
    x21, y21 = x20 + x19, y20 + y19
    x22, y22 = x21 + x20, y21 + y20
    x23, y23 = x22 + x21, y22 + y21
    x24, y24 = x23 + x22, y23 + y22
    x25, y25 = x24 + x23, y24 + y23
    x26, y26 = x25 + x24, y25 + y24
    x27, y27 = x26 + x25, y26 + y25
    x28

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if abs(x1 - x2) + abs(y1 - y2) == 2:
        print("Yes")
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x1 - x2
    dy = y1 - y2
    dx, dy = abs(dx), abs(dy)
    if dx == 0 and dy == 0:
        print('No')
    elif dx == dy:
        print('Yes')
    elif dx == 0 or dy == 0:
        print('Yes')
    elif dx % 2 == 0 and dy % 2 == 0:
        print('Yes')
    elif dx % 2 == 1 and dy % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("Yes")
    elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 入力
    x1, y1, x2, y2 = map(int, input().split())
    # 出力
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("No")
        return

    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print("Yes")
    print(x3, y3, x4, y4)

=======
Suggestion 10

def main():
    x1, y1, x2, y2 = map(int, input().split())
    #print(x1, y1, x2, y2)
    #print(abs(x1-x2), abs(y1-y2))
    if abs(x1-x2) + abs(y1-y2) == 5:
        print("Yes")
    elif abs(x1-x2) + abs(y1-y2) == 3:
        print("Yes")
    elif abs(x1-x2) + abs(y1-y2) == 1:
        print("Yes")
    else:
        print("No")
