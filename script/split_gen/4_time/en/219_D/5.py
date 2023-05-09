def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[[False for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    dp[i+1][min(j+a[i], x)][min(k+b[i], y)] = True
    for i in range(x, x+1):
        for j in range(y, y+1):
            if dp[n][i][j]:
                print(n)
                return
    print(-1)
