Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if X > Y:
        print(0)
    else:
        print((Y - X + 9) // 10)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    print(max(0, (y + 9) // 10 - (x + 9) // 10))

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    print((Y + 9) // 10 - X // 10)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    print((Y - 1) // 10 - X // 10)

=======
Suggestion 5

def main():
    x,y = map(int,input().split())
    if y % 10 == 0:
        if y <= x:
            print(0)
        else:
            print((y-x)//10)
    else:
        if y <= x:
            print(0)
        else:
            print((y-x)//10+1)

=======
Suggestion 6

def main():
    #入力
    x, y = map(int, input().split())
    #計算
    ans = (y - x + 9) // 10
    #出力
    print(ans)

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    print((Y-X+9)//10)

=======
Suggestion 8

def main():
    # 1行目の入力
    X, Y = map(int, input().split())
    # ここに処理を書く
    if X >= Y:
        print(0)
    else:
        print((Y - X + 9) // 10)

=======
Suggestion 9

def main():
    x, y = map(int, input().split())

    # 10円切手の枚数
    count = 0

    # 10円切手を貼り付ける
    while x < y:
        x += 10
        count += 1

    print(count)
