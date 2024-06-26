def main():
    L = int(input())
    dp = [[0 for _ in range(L+1)] for _ in range(L+1)]
    dp[0][0] = 1
    for i in range(L):
        for j in range(L):
            if dp[i][j] == 0:
                continue
            for k in range(j, L):
                dp[i+1][k] += dp[i][j]
    print(dp[L][L] - 1)
