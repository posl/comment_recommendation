def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N):
        for j in range(K):
            if i + A[j] <= N:
                dp[i + A[j]] = 1 - dp[i]
            else:
                break
    if dp[N] == 0:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    solve()