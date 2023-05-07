def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    paths = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        paths[u].append(v)
        paths[v].append(u)
    path = [None] * N
    path[X] = 0
    stack = [X]
    while stack:
        x = stack.pop()
        for y in paths[x]:
            if path[y] is None:
                path[y] = path[x] + 1
                stack.append(y)
    ans = [0] * N
    for i in range(N):
        if i != X:
            ans[path[i]] += 1
    print(' '.join(map(str, ans)))
