def main():
    N = int(input())
    Snuke = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snuke.append([T, X, A])
    Snuke = sorted(Snuke, key=lambda x: x[0])
    #print(Snuke)
    dp = [[0] * 5 for i in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if Snuke[i][1] == j:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + Snuke[i][2])
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1])
            if j < 4:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j+1])
    #print(dp)
    print(max(dp[-1]))
