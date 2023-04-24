Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, Q + R, R + P))

=======
Suggestion 2

def main():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 3

def main():
    # 入力
    P, Q, R = map(int, input().split())
    # 出力
    print(min(P + Q, Q + R, R + P))

=======
Suggestion 4

def main():
    P,Q,R = map(int,input().split())
    print(min(P+Q,P+R,Q+R))

=======
Suggestion 5

def solve(p,q,r):
    return min(p+q,p+r,q+r)
