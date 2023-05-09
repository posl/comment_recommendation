def main():
    n, m = map(int, input().split())
    edge = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        edge[u - 1][v - 1] = 1
        edge[v - 1][u - 1] = 1
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if edge[i][j] and edge[j][k] and edge[k][i]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()