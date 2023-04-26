Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print((Y - X + 9) // 10)

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    print((Y - X + 9) // 10)

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if X % 10 == 0:
        print(0)
    else:
        print(10 - X % 10)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
        return
    print((Y - X + 9) // 10)

=======
Suggestion 5

def main():
    #入力
    X, Y = map(int, input().split())
    #計算
    ans = 0
    if Y % 10 != 0:
        ans = (Y // 10 + 1) * 10 - X
    else:
        ans = Y - X
    #出力
    print(ans)

=======
Suggestion 6

def main():
    x,y = map(int,input().split())
    print(max(0,((y-x-1)//10)+1))

=======
Suggestion 7

def main():
    x, y = map(int, input().split()) # x=80, y=94
    print((y-x+9)//10)

=======
Suggestion 8

def main():
    # 1行目に入力される文字列を取得
    line = input()
    # 1行目に入力された文字列をスペースで分割
    X, Y = line.split(" ")
    # 文字列を整数に変換
    X = int(X)
    Y = int(Y)
    
    # 10円切手を貼り足す枚数を求める
    answer = (Y - X) // 10
    
    # 答えを出力
    print(answer)
