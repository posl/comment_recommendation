def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        G[A[i] - 1].append(B[i] - 1)
    V = [0] * N
    P = []
    for i in range(N):
        if V[i] == 0:
            if not dfs(i, G, V, P):
                print(-1)
                return
    P = P[::-1]
    print(*[x + 1 for x in P])

if __name__ == '__main__':
    main()