def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    mod = 10**9+7
    N,M = map(int,input().split())
    if M == 0:
        print(0)
        return
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    dist = [-1]*(N+1)
    dist[1] = 0
    q = deque()
    q.append(1)
    path = [0]*(N+1)
    path[1] = 1
    while q:
        now = q.popleft()
        for nex in G[now]:
            if dist[nex] == -1:
                dist[nex] = dist[now] + 1
                path[nex] = path[now]
                q.append(nex)
            elif dist[nex] == dist[now] + 1:
                path[nex] += path[now]
                path[nex] %= mod
    print(path[N])

if __name__ == '__main__':
    main()