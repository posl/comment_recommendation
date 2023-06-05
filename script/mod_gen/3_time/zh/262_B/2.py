def solve():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    # print(edges)
    cnt = 0
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if edges[i][0] in edges[j] and edges[i][1] in edges[j]:
                cnt += 1
                # print(edges[i], edges[j])
    print(int(cnt/3))
solve()
