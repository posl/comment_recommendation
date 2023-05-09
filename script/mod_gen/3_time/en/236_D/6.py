def main():
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(1 << n):
            if j >> i & 1:
                continue
            for k in range(i + 1, n):
                if j >> k & 1:
                    continue
                dp[i][j] = max(dp[i][j], dp[i + 1][j | 1 << i | 1 << k] ^ a[i][k - i - 1])
    print(dp[0][0])

if __name__ == '__main__':
    main()