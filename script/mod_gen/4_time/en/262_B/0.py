def main():
    N, M = map(int, input().split())
    G = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] = 1
        G[v-1][u-1] = 1
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if G[i][j] == 0:
                continue
            for k in range(j+1, N):
                if G[i][k] == 0:
                    continue
                if G[j][k] == 0:
                    continue
                count += 1
    print(count)

if __name__ == '__main__':
    main()