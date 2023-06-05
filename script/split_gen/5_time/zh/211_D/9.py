def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 1からNへの最短経路長を求める
    from collections import deque
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1: continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    # 1からNへの最短経路長が最大となるような辺を列挙する
    max_dist = max(dist)
    edges = []
    for a, b in AB:
        if dist[a - 1] == max_dist and dist[b - 1] == max_dist:
            edges.append((a - 1, b - 1))
    # 1からNへの最短経路長が最大となるような辺の数を数える
    from collections import defaultdict
    cnt = defaultdict(int)
    for a, b in edges:
        cnt[a] += 1
        cnt[b] += 1
    # 1からNへの最短経路長が最大となるような辺の数が最大となるような辺を列挙する
    max_cnt = max(cnt.values())
    ans = []
    for a, b in edges:
        if cnt[a] == max_cnt and cnt[b] == max_cnt:
            ans.append((a, b))
    print(len(ans))
