def main():
    N = int(input())
    Snuke = [[int(i) for i in input().split()] for _ in range(N)]
    Snuke.sort()
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            if Snuke[i-1][0] >= abs(j-Snuke[i-1][1]):
                dp[i][j] = max(dp[i][j], dp[i-1][Snuke[i-1][1]] + Snuke[i-1][2])
    print(max(dp[N]))
