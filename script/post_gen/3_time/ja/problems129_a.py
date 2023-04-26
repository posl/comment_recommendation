Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 2

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, Q + R, R + P))

=======
Suggestion 3

def solve():
    p, q, r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 4

def main():
    # 標準入力の取得
    p, q, r = map(int, input().split())

    # 飛行時間の和の最小値を出力
    print(min(p + q, q + r, r + p))
