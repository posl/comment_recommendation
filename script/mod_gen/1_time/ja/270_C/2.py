def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        if i == Y:
            ans[i] = abs(i - X)
        else:
            ans[i] = bfs(i, X, Y, edge)
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()