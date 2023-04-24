Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    l, r = map(int, input().split())
    s = "atcoder"
    print(s[l-1:r])

=======
Suggestion 2

def main():
    l, r = map(int, input().split())
    print('atcoder'[l - 1:r])

=======
Suggestion 3

def main():
    L,R = map(int,input().split())
    S = "atcoder"
    print(S[L-1:R])

=======
Suggestion 4

def main():
    # 入力
    L, R = map(int, input().split())

    # 出力
    print("atcoder"[L-1:R])

=======
Suggestion 5

def main():
    L, R = map(int, input().split())
    print(input()[L-1:R])

=======
Suggestion 6

def solve():
    L, R = map(int, input().split())
    print("atcoder"[L-1:R])

=======
Suggestion 7

def main():
    s = input()
    l, r = map(int, s.split())
    print("atcoder"[l - 1:r])

=======
Suggestion 8

def main():
    # 文字列を取得
    atcoder = input()
    # L,Rを取得
    L, R = map(int, input().split())
    # 文字列のL文字目からR文字目までを出力
    print(atcoder[L-1:R])

=======
Suggestion 9

def main():
    #atcoderの文字列を定義
    atcoder = "atcoder"

    #入力
    L,R = map(int,input().split())

    #L文字目からR文字目までを出力
    print(atcoder[L-1:R])

=======
Suggestion 10

def main():
    L,R = map(int,input().split())
    list = "atcoder"
    print(list[L-1:R])
