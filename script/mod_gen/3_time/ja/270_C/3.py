def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        x = que.pop()
        for y in tree[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                que.append(y)
    for i in range(N):
        if dist[i] == -1:
            dist[i] = dist[Y] + 1
            que.append(i)
    while que:
        x = que.pop()
        for y in tree[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                que.append(y)
    ans = [0] * (N-1)
    for i in range(N):
        if i != X:
            ans[dist[i]-1] += 1
    print(*ans)

if __name__ == '__main__':
    main()