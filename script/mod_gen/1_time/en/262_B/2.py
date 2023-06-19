def main():
    n, m = map(int, input().split())
    g = [[0] * n for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
        g[b-1][a-1] = 1
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if g[i][j] == 1 and g[i][k] == 1 and g[j][k] == 1:
                    ans += 1
    print(ans)
main()
