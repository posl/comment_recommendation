def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    dist = [-1] * N
    dist[0] = 0
    queue = [0]
    while queue:
        v = queue.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 0
    mod = 10**9 + 7
    dp = [0] * N
    dp[0] = 1
    for d in range(1, dist[-1]+1):
        for v in range(N):
            if dist[v] == d:
                for nv in G[v]:
                    if dist[nv] == d-1:
                        dp[v] += dp[nv]
                        dp[v] %= mod
    print(dp[-1])

if __name__ == '__main__':
    main()