Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[:K]))

=======
Suggestion 4

def main():
    # 入力
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 処理
    p.sort()
    ans = sum(p[:K])
    # 出力
    print(ans)

=======
Suggestion 5

def main():
    #入力
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #ソート
    p.sort()
    #出力
    print(sum(p[0:K]))
