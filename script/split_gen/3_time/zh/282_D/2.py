def solve():
    N,M = map(int,input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int,input().split())))
    edge.sort()
    ans = 0
    black = [0] * (N+1)
    white = [0] * (N+1)
    for i in range(M):
        u = edge[i][0]
        v = edge[i][1]
        if (black[u] == 0 and black[v] == 0) or (white[u] == 0 and white[v] == 0):
            ans += 1
            black[u] = 1
            black[v] = 1
        white[u] = 1
        white[v] = 1
    print(ans)
    return 0
