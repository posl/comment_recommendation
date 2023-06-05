def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))
    # print(ab)
    # 1からの最短経路を求める
    from collections import deque
    adj = [[] for _ in range(n + 1)]
    for a, b in ab:
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)
    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            queue.append(nv)
    # print(dist)
    # 1からの最短経路から逆算していく
    ans = [0] * (n + 1)
    for a, b in ab:
        # 1からの最短経路が繋がっているか
        if dist[a] == dist[b] + 1:
            ans[a] = b
        if dist[b] == dist[a] + 1:
            ans[b] = a
    # print(ans)
    # 全部埋まっているか
    if 0 in ans[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, n + 1):
            print(ans[i])

if __name__ == '__main__':
    main()