def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    edge = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in edge[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[N - 1] == -1:
        print(0)
        return
    ans = 0
    for i in range(N):
        if dist[i] == dist[N - 1] - 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()