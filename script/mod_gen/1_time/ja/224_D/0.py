def main():
    M = int(input())
    G = [[0] * 9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1
    p = list(map(int, input().split()))
    for i in range(8):
        G[p[i] - 1][p[i + 1] - 1] = 1
        G[p[i + 1] - 1][p[i] - 1] = 1
    for i in range(9):
        G[i][i] = 1
    for k in range(9):
        for i in range(9):
            for j in range(9):
                G[i][j] |= G[i][k] & G[k][j]
    if G[0][1] & G[1][2] & G[2][3] & G[3][4] & G[4][5] & G[5][6] & G[6][7] & G[7][8]:
        print(0)
    else:
        print(-1)

if __name__ == '__main__':
    main()