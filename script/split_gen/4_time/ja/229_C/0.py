def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - A[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - A[i]] + B[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
    print(dp[N][W])
