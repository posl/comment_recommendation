def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    dp = [[0]*(2**N) for _ in range(N+1)]
    for i in range(2**N):
        for j in range(N):
            if (i>>j)&1:
                for k in range(j+1, N):
                    if (i>>k)&1:
                        dp[j+1][i] = max(dp[j+1][i], dp[j][i-(1<<j)-(1<<k)]+A[j][k])
    print(dp[N][(2**N)-1])
