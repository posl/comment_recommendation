def solve():
    n, m = map(int, input().split())
    # 邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 队列
    q = [0]
    # 距离
    dist = [0]+[float('inf')]*(n-1)
    # 记录路径条数
    cnt = [0]*n
    cnt[0] = 1
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u]+1
                q.append(v)
                cnt[v] = cnt[u]
            elif dist[v] == dist[u]+1:
                cnt[v] += cnt[u]
    print(cnt[-1] % (10**9+7))

if __name__ == '__main__':
    solve()