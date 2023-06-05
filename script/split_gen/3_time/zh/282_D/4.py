def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[1])
    cnt = 0
    for i in range(m):
        for j in range(i + 1, m):
            if edges[i][0] != edges[j][0] and edges[i][1] != edges[j][1]:
                cnt += 1
    print(cnt)
