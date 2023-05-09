def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for s in range(1 << N):
            if s >> i & 1:
                for j in range(N):
                    if s >> j & 1:
                        dp[i][s] = max(dp[i][s], dp[i + 1][s ^ (1 << i)] + A[i][j])
    print(dp[0][-1])
