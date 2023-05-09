def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リストを作る
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)
    # BFS
    from collections import deque
    q = deque()
    q.append(1)
    dist = [-1] * (N+1)
    dist[1] = 0
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    for c, d in CD:
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
