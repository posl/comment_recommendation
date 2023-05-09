def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    print(*dfs(X, Y, G))

if __name__ == '__main__':
    main()