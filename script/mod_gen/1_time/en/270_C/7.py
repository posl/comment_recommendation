def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #X -= 1
    #Y -= 1
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    #print(adj)
    dist = [-1] * N
    dist[X-1] = 0
    que = [X-1]
    while que:
        v = que.pop(0)
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    #print(dist)
    ans = [0] * N
    for i in range(N):
        if dist[i] != -1:
            ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

if __name__ == '__main__':
    main()