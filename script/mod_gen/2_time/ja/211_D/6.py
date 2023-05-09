def main():
    import sys
    readline = sys.stdin.readline
    from collections import deque
    from itertools import permutations
    mod = 10**9+7
    N,M = map(int,readline().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for i in range(M):
        a,b = map(int,readline().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 1からNまでの最短距離を求める
    dist = [-1]*N
    dist[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    # 1からNまでの最短距離がKのものを数える
    K = dist[N-1]
    cnt = 0
    for i in range(N):
        if dist[i] == K:
            cnt += 1
    # 1からNまでの最短距離がKのもののうち、1からNまでの最短経路を数える
    ans = 1
    for i in range(N):
        if dist[i] == K:
            ans = ans*len(G[i])
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()