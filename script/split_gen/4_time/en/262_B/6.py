def solve():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append([u, v])
    ans = 0
    for i in range(M):
        u, v = edges[i]
        for j in range(M):
            if i == j:
                continue
            if u in edges[j] and v in edges[j]:
                ans += 1
    print(ans//6)
