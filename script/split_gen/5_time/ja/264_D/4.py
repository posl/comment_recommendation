def main():
    S = input()
    T = "atcoder"
    dp = [[0] * (len(S) + 1) for _ in range(len(T) + 1)]
    for i in range(len(T)):
        for j in range(len(S)):
            if T[i] == S[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    print(len(S) - dp[-1][-1])
