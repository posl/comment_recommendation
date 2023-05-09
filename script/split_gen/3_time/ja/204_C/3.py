def main():
    n, m = map(int, input().split())
    g = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                for k in range(n):
                    if g[j][k] == 1 and g[k][i] == 1:
                        ans += 1
    print(ans)
