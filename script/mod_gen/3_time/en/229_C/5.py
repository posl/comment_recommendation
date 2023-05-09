def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, 0, -1):
            if j - B[i] >= 0:
                dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

if __name__ == '__main__':
    solve()