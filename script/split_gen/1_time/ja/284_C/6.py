def main():
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        u, v = map(int, input().split())
        edge.append((u, v))
    if M == 0:
        print(N)
        return
    edge.sort()
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def unite(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            x, y = y, x
        if rank[x] == rank[y]:
            rank[x] += 1
        parent[y] = x
        return True
    def same(x, y):
        return find(x) == find(y)
    parent = [i for i in range(N+1)]
    rank = [0 for i in range(N+1)]
    for u, v in edge:
        unite(u, v)
    ans = 0
    for i in range(1, N+1):
        if parent[i] == i:
            ans += 1
    print(ans)
