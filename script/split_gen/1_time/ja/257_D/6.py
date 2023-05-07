def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    jump = [list(map(int, input().split())) for _ in range(N)]
    jump.sort(key=lambda x:x[2])
    jump = [[0, 0, 0]] + jump
    # dp[i][j]: i番目のジャンプ台からj番目のジャンプ台に移動するために必要な最小訓練回数
    # dp[i][j] = min(dp[i][k] + dp[k][j]) (i < k < j)
    dp = [[float('inf')] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(i, j):
                x1, y1, p1 = jump[i]
                x2, y2, p2 = jump[j]
                x3, y3, p3 = jump[k]
                if p1 * (j-i) >= abs(x1-x2) + abs(y1-y2) and p3 * (j-i) >= abs(x3-x2) + abs(y3-y2):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + 1)
    print(min(dp[1]))
