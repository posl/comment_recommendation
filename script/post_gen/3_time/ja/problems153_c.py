Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if N <= K:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = 0
    for i in range(N-K):
        ans += H[i]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            continue
        ans += H[i]
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)

    if N <= K:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = sorted(H,reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            continue
        else:
            ans += H[i]
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    for i in range(K):
        if i >= N:
            break
        H[i] = 0
    print(sum(H))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    # 降順にソート
    H.sort(reverse=True)

    # モンスターの体力が 0 以下になるまでの攻撃回数を出力
    print(max(0, sum(H) - K))
