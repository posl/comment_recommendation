Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pqr = input().split()
    p = int(pqr[0])
    q = int(pqr[1])
    r = int(pqr[2])
    print(min(p+q, q+r, r+p))

=======
Suggestion 2

def main():
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))

=======
Suggestion 3

def main():
    p, q, r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 4

def main():
    # 標準入力から値を取得する
    p, q, r = map(int, input().split())
    # 飛行時間の和の最小値を出力
    print(min(p+q, q+r, r+p))

=======
Suggestion 5

def main():
    P,Q,R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))
    return

=======
Suggestion 6

def main():
    P,Q,R = map(int,input().split())
    print(min(P+Q,Q+R,R+P))
main()

=======
Suggestion 7

def main():
    # P, Q, R = map(int, input().split())
    # print(min(P+Q, Q+R, R+P))
    print(min([sum(x) for x in zip(map(int, input().split()), map(int, input().split()), map(int, input().split()))]))

=======
Suggestion 8

def main():
    p,q,r = map(int,input().split())
    print(min(p+q,r+p,r+q))
