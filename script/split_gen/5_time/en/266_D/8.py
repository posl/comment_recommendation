def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    #print(N, S)
    #dp = [[0 for _ in range(5)] for _ in range(N+1)]
    dp = [[0 for _ in range(5)] for _ in range(N)]
    #print(dp)
    for i in range(N):
        for j in range(5):
            if j == S[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + S[i][2])
            elif j >= 1 and dp[i-1][j-1] > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + S[i][2])
            elif j <= 3 and dp[i-1][j+1] > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j+1] + S[i][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
    #print(dp)
    print(max(dp[N-1]))
