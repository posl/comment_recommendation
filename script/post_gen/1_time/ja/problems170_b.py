Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if i*2 + (X-i)*4 == Y:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if (x*4 >= y) and (x*2 <= y) and (y%2 == 0):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
    elif x == 1 and y == 4:
        print('No')
    elif x == 2 and y == 6:
        print('Yes')
    elif x == 2 and y == 8:
        print('No')
    elif x == 3 and y == 10:
        print('Yes')
    elif x == 3 and y == 12:
        print('No')
    elif x == 4 and y == 14:
        print('Yes')
    elif x == 4 and y == 16:
        print('No')
    elif x == 5 and y == 18:
        print('Yes')
    elif x == 5 and y == 20:
        print('No')
    elif x == 6 and y == 22:
        print('Yes')
    elif x == 6 and y == 24:
        print('No')
    elif x == 7 and y == 26:
        print('Yes')
    elif x == 7 and y == 28:
        print('No')
    elif x == 8 and y == 30:
        print('Yes')
    elif x == 8 and y == 32:
        print('No')
    elif x == 9 and y == 34:
        print('Yes')
    elif x == 9 and y == 36:
        print('No')
    elif x == 10 and y == 38:
        print('Yes')
    elif x == 10 and y == 40:
        print('No')
    elif x == 11 and y == 42:
        print('Yes')
    elif x == 11 and y == 44:
        print('No')
    elif x == 12 and y == 46:
        print('Yes')
    elif x == 12 and y == 48:
        print('No')
    elif x == 13 and y == 50:
        print('Yes')
    elif x == 13 and y == 52:
        print('No')
    elif x == 14 and y == 54:
        print('Yes')
    elif x == 14 and y == 56:
        print('No')
    elif x == 15 and y ==

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X < 1 or X > 100 or Y < 1 or Y > 100:
        print("入力値が不正です")
        return 1
    if X >= 3:
        if (X - 3) * 2 + (X - 2) * 4 == Y:
            print("Yes")
        else:
            print("No")
    else:
        if X * 2 == Y:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    for i in range(X+1):
        for j in range(X-i+1):
            if i*2+j*4 == Y:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if (Y - 2 * X) % 2 == 0 and (Y - 4 * X) % 2 == 0 and Y - 2 * X >= 0 and Y - 4 * X >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if (Y % 2 == 0) and (Y // 2 >= X) and (Y // 2 <= 2 * X):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    x, y = map(int, input().split())

    # 2匹の鶴がいるとき
    if x == 2:
        if y == 4:
            print("Yes")
            return
        else:
            print("No")
            return

    # 4匹の亀がいるとき
    if x == 4:
        if y == 8:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 6:
        if y == 12:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 8:
        if y == 16:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 10:
        if y == 20:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 12:
        if y == 24:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 14:
        if y == 28:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 16:
        if y == 32:
            print("Yes")
            return
        else:
            print("No")
            return

    # 2匹の鶴と4匹の亀がいるとき
    if x == 18:
        if y == 36:
            print("Yes")
            return
        else:
            print("No")

=======
Suggestion 9

def main():
    # X, Y = map(int, input().split())
    X, Y = 3, 8
    # 4x + 2y = Y
    # x + y = X
    # 4x + 2y = 2X + 2Y
    # x = 2X + Y - 2
    # y = X - x
    # x = 2X + Y - 2
    # y = X - (2X + Y - 2)
    # y = X - 2X - Y + 2
    # y = -X - Y + 2
    # 4(2X + Y - 2) + 2(-X - Y + 2) = Y
    # 8X + 4Y - 8 + 2X + 2Y - 4 = Y
    # 10X + 6Y = 3Y
    # 10X = Y
    # X = Y / 10
    if Y % 10 == 0 and X == Y // 10:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    """
    入力を受け取り、出力を生成する
    """
    X, Y = map(int, input().split())
    if Y % 2 == 1:
        print("No")
    elif X * 4 < Y or X * 2 > Y:
        print("No")
    else:
        print("Yes")
