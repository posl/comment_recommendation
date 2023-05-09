def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = [[0, 0] for _ in range(M)]
    for i in range(M):
        bonus[i] = list(map(int, input().split()))
    bonus.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + bonus[j][0] > N:
                break
            dp[i + bonus[j][0]] = max(dp[i + bonus[j][0]], dp[i] + bonus[j][1])
    print(dp[N])

if __name__ == '__main__':
    main()