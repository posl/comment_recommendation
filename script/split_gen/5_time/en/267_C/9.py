def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    # dp[i] := Aのi番目までの要素を使って、連続する要素の和の最大値
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i] + A[i], A[i])
    # dp[i] := Aのi番目までの要素を使って、連続する要素の和の最大値
    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = max(dp2[i], dp[i + 1])
    ans = 0
    for i in range(1, N + 1):
        if i - M >= 0:
            ans = max(ans, dp[i] + dp2[i - M])
        else:
            ans = max(ans, dp[i])
    print(ans)
