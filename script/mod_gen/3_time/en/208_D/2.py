def main():
    N, M = map(int, input().split())
    G = [[float('inf')] * N for i in range(N)]
    for i in range(N):
        G[i][i] = 0
    for i in range(M):
        A, B, C = map(int, input().split())
        G[A-1][B-1] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][k] + G[k][j] == G[i][j]:
                    ans += G[i][j]
                    break
    print(ans)

if __name__ == '__main__':
    main()