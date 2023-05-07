def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(1 << N):
            if j & (1 << i):
                continue
            for k in range(i + 1, N):
                if j & (1 << k):
                    continue
                dp[i + 1][j | (1 << i) | (1 << k)] = max(dp[i + 1][j | (1 << i) | (1 << k)], dp[i][j] ^ A[i][k])
    print(dp[N][(1 << N) - 1])

if __name__ == '__main__':
    main()