def main():
    N = int(input())
    Snuke = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snuke.append((T, X, A))
    Snuke.sort()
    dp = [[0 for j in range(5)] for i in range(N)]
    for i in range(N):
        for j in range(5):
            if i == 0:
                if Snuke[i][1] == j:
                    dp[i][j] = Snuke[i][2]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j]
                if Snuke[i][1] == j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + Snuke[i][2])
                if Snuke[i][1] == j - 1 and Snuke[i][0] - Snuke[i - 1][0] >= abs(j - (j - 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + Snuke[i][2])
                if Snuke[i][1] == j + 1 and Snuke[i][0] - Snuke[i - 1][0] >= abs(j - (j + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + Snuke[i][2])
    print(max(dp[N - 1]))

if __name__ == '__main__':
    main()