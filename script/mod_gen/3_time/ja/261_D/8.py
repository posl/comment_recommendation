def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(M)]
    B.sort(key=lambda x: -x[1])
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if B[j][0] <= i + 1:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - B[j][0]] + B[j][1])
    print(dp[-1])

if __name__ == '__main__':
    main()