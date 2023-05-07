def main():
    N, M = map(int, input().split())
    edges = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edges[u-1][v-1] = 1
        edges[v-1][u-1] = 1
    ans = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if edges[a][b] == 1 and edges[b][c] == 1 and edges[c][a] == 1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()