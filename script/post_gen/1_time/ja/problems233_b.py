Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 2

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 3

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print(''.join(S))

=======
Suggestion 4

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print("".join(S))

=======
Suggestion 5

def main():
    #入力
    L, R = map(int, input().split())
    S = input()
    #処理
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    #出力
    print(S)

=======
Suggestion 6

def main():
    # L R
    # S
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1]+S[L-1:R][::-1]+S[R:])

=======
Suggestion 7

def main():
    #入力
    L, R = map(int, input().split())
    S = input()
    #L-1文字目までとR文字目以降を別々に取得
    front = S[:L-1]
    back = S[R:]
    #L-1文字目からR文字目までを反転して取得
    middle = S[L-1:R][::-1]
    #結合して出力
    print(front + middle + back)
