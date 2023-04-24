Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

main()

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
    ans = float("inf")
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    hs = [int(input()) for _ in range(N)]
    hs.sort()
    min_diff = 10 ** 9
    for i in range(N - K + 1):
        min_diff = min(min_diff, hs[i + K - 1] - hs[i])
    print(min_diff)

=======
Suggestion 6

def main():
    # 入力
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]

    # 計算
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])

    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort() #昇順にソート
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]

    #ソート
    h.sort()

    #各区間の最小値を求める
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])

    #出力
    print(ans)
