Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    #入力
    N,K = map(int,input().split())
    h = [int(input()) for i in range(N)]

    #ソート
    h.sort()

    #答え
    ans = 10**9

    #高さの差の最小値を求める
    for i in range(N-K+1):
        ans = min(ans,h[i+K-1]-h[i])

    #出力
    print(ans)
