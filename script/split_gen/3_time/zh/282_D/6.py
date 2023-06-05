def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u-1].append(v-1)
        adj_list[v-1].append(u-1)
    for i in range(n):
        adj_list[i].sort()
    ans = 0
    for u, v in edges:
        if len(adj_list[u-1]) > len(adj_list[v-1]):
            u, v = v, u
        for w in adj_list[u-1]:
            if w in adj_list[v-1]:
                ans += 1
    print(ans)
solve()
