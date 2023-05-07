def main():
    N = int(input())
    x, y, p = [], [], []
    for _ in range(N):
        xi, yi, pi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        p.append(pi)
    #print(x, y, p)
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if p[i] * (i + 1) >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                dp[i][j] = 1
    #print(dp)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] == 1 and dp[k][j] == 1:
                    dp[i][j] = 1
    #print(dp)
    ans = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == 1:
                ans = max(ans, i + 1)
    print(ans)
