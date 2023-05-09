def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for i in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        v = que.pop()
        for u in edge[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            que.append(u)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            continue
        print(ans[i])

if __name__ == '__main__':
    main()