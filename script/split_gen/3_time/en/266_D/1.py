def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #dp[t][x] := t時点でxにいる時の最大の取得可能なスヌーケの合計サイズ
    dp = [[0] * 5 for _ in range(10 ** 5 + 1)]
    for i in range(N):
        for j in range(5):
            dp[T[i]][j] = max(dp[T[i]][j], dp[T[i] - 1][j])
        dp[T[i]][X[i]] = max(dp[T[i]][X[i]], dp[T[i] - 1][X[i]] + A[i])
    print(max(dp[T[-1]]))
