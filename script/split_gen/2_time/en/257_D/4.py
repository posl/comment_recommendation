def main():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    # dp[i][j] := i回目の訓練で、j番目のトランポリンに到達できるか
    dp = [[False] * N for i in range(2000)]
    dp[0][0] = True
    for i in range(1999):
        for j in range(N):
            if dp[i][j]:
                for k in range(N):
                    if p[j] * i >= abs(x[j] - x[k]) + abs(y[j] - y[k]):
                        dp[i + 1][k] = True
    for i in range(2000):
        if dp[i][N - 1]:
            print(i)
            return
