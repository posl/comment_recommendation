def main():
    n, m = map(int, input().split())
    edge = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u][v] = 1
        edge[v][u] = 1
    for i in range(n):
        for j in range(i + 1, n):
            if edge[i][j] == 1:
                for k in range(j + 1, n):
                    if edge[i][k] == 1 and edge[j][k] == 1:
                        print('No')
                        return
    print('Yes')
    return

if __name__ == '__main__':
    main()