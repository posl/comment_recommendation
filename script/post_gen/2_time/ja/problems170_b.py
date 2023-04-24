Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x * 4 < y or y < x * 2:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X*2 <= Y <= X*4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if 4 * X - Y >= 0 and 4 * X - Y <= 4 * X and Y % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #入力
    X, Y = map(int, input().split())
    #鶴の数
    t = 0
    #亀の数
    k = 0
    #鶴の数が2匹以上のとき
    while t < X:
        #鶴の数を1匹ずつ増やす
        t += 1
        #亀の数を計算
        k = X - t
        #足の数が合っているか確認
        if 2 * t + 4 * k == Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    # 鶴と亀の数
    X, Y = map(int, input().split())
    # 鶴の数
    t = 0
    # 亀の数
    k = 0

    # 鶴の数を変化させる
    for i in range(X + 1):
        t = i
        # 亀の数を計算する
        k = X - t
        # 足の本数が合致するか判定する
        if t * 2 + k * 4 == Y:
            print("Yes")
            exit(0)
    # どちらも該当しない場合
    print("No")

=======
Suggestion 9

def main():
    #入力
    X, Y = map(int, input().split())
    #足の本数の差を計算
    diff = Y - 2 * X
    #亀の数を計算
    turtle = diff // 2
    #鶴の数を計算
    crane = X - turtle
    #亀と鶴の数が正しいか判定
    if turtle >= 0 and crane >= 0 and 4 * turtle + 2 * crane == Y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # 鶴と亀の数の組合せ
    # 2匹の鶴がいる場合は、4匹の亀がいる
    # 亀の数は、(足の数 - 鶴の数 * 2) / 2
    # 亀の数が0以下の場合は、鶴と亀の数の組合せは存在しない
    # 亀の数が整数でない場合は、鶴と亀の数の組合せは存在しない
    x, y = map(int, input().split())
    if x * 2 <= y <= x * 4:
        if (y - x * 2) % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
