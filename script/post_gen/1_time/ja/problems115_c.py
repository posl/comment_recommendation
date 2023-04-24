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
    ans = h[-1] - h[0]
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = h[N-1] - h[0]
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()

    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])

    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()

    min_diff = float('inf')
    for i in range(N - K + 1):
        diff = h[i + K - 1] - h[i]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

=======
Suggestion 6

def main():
    # 入力
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]

    # h を昇順にソート
    h.sort()

    # h の差の絶対値の最小値を求める
    ans = 10 ** 9 + 1
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])

    # 出力
    print(ans)
