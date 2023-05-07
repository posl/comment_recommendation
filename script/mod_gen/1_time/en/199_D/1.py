def main():
    N, M = list(map(int, input().split()))
    G = [[] for i in range(N)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    print(dfs(G, 0, [-1 for i in range(N)]))

if __name__ == '__main__':
    main()