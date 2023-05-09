def main():
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if S[i][0] == i+1:
            dp[i+1][S[i][1]] = max(dp[i+1][S[i][1]], dp[i][S[i][1]] + S[i][2])
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + S[i][2])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()