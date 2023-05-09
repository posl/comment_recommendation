def main():
    N = int(input())
    S = input()
    # 1-indexed
    S = " " + S
    # dp[i] = maximum non-negative integer l that satisfies
    # l + i <= N and for all integers k such that 1 <= k <= l,
    # it holds that S_k != S_{k+i}
    dp = [0] * (N + 1)
    # dp[i] = max(dp[i], dp[i + 1] - 1) when S[i] == S[i + 1]
    for i in range(1, N):
        if S[i] == S[i + 1]:
            dp[i + 1] = max(dp[i + 1], dp[i] - 1)
    # dp[i] = max(dp[i], dp[i + 1] + 1) when S[i] != S[i + 1]
    for i in range(1, N):
        if S[i] != S[i + 1]:
            dp[i + 1] = max(dp[i + 1], dp[i] + 1)
    print(*dp[1:], sep="
")
