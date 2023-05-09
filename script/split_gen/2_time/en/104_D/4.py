def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    dp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if S[i] == "?":
                    for l in range(3):
                        dp[i+1][(j+l)%3][(k+l)%3] += dp[i][j][k]
                        dp[i+1][(j+l)%3][(k+l)%3] %= MOD
                else:
                    l = ord(S[i]) - ord("A")
                    dp[i+1][(j+l)%3][(k+l)%3] += dp[i][j][k]
                    dp[i+1][(j+l)%3][(k+l)%3] %= MOD
    print(dp[N][0][0])
