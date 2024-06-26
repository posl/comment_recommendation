def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(1 << N):
            if j >> i & 1:
                continue
            for k in range(i + 1, N):
                if j >> k & 1:
                    continue
                dp[i][j] = max(dp[i][j], dp[i + 1][j | 1 << i | 1 << k] ^ A[i][k])
    print(dp[0][0])

if __name__ == '__main__':
    main()