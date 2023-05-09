def solve():
    N, W = map(int, input().split())
    items = []
    for i in range(N):
        A, B = map(int, input().split())
        items.append((A, B))
    dp = [0] * (W + 1)
    for i in range(N):
        A, B = items[i]
        for w in range(W, -1, -1):
            if w >= A:
                dp[w] = max(dp[w], dp[w - A] + B)
    print(dp[W])

if __name__ == '__main__':
    solve()