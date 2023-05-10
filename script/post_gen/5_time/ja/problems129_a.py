Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 標準入力から値を取得する
    p, q, r = map(int, input().split())
    
    # ここにプログラムを追記
    # 経路は6通りある
    # A->B->C
    # A->C->B
    # B->A->C
    # B->C->A
    # C->A->B
    #

=======
Suggestion 2

def main():
    # データ入力
    p,q,r = map(int,input().split())

    # 出力
    print(min(p+q,q+r,r+p))

=======
Suggestion 3

def main():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 4

def main():
    # input
    P, Q, R = map(int, input().split())

    # compute
    ans = P + Q + R - max(P, Q, R)

    # output
    print(ans)

=======
Suggestion 5

def main():
    pqr = list(map(int, input().split()))
    pqr.sort()
    print(pqr[0] + pqr[1])

=======
Suggestion 6

def main():
    # input
    P, Q, R = map(int, input().split())

    # compute
    ans = min(P+Q, Q+R, R+P)

    # output
    print(ans)

=======
Suggestion 7

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, P + R, Q + R))
