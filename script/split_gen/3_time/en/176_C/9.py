def main():
    N = int(input())
    A = list(map(int, input().split()))
    # dp[i][j] := i番目の人がjの高さのstoolを持つときの、stoolの合計高さの最小値
    # 0 <= j <= A[i]
    dp = [[float('inf')] * (max(A) + 1) for _ in range(N)]
    dp[0][0] = 0
    dp[0][A[0]] = A[0]
    for i in range(1, N):
        for j in range(max(A) + 1):
            if j < A[i]:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][A[i]] + j)
            else:
                dp[i][j] = dp[i - 1][j]
    print(min(dp[-1]))
