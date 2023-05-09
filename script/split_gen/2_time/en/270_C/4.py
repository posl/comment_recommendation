def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    path = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        path[u].append(v)
        path[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        d = [0] * N
        q = [i]
        while q:
            x = q.pop()
            for y in path[x]:
                if d[y] == 0:
                    d[y] = d[x] + 1
                    q.append(y)
        ans[d[Y]] += 1
    for i in range(1, N):
        print(ans[i])
