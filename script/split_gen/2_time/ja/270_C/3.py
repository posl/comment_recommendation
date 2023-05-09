def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        tree[U].append(V)
        tree[V].append(U)
    dist = [0] * N
    dist[X] = 1
    que = [X]
    while que:
        node = que.pop(0)
        for child in tree[node]:
            if dist[child] == 0:
                dist[child] = dist[node] + 1
                que.append(child)
    ans = []
    for i in range(N):
        if i == X or i == Y:
            continue
        if dist[i] == 0:
            continue
        if dist[i] == dist[Y] + 1:
            ans.append(i+1)
    print(*ans)
