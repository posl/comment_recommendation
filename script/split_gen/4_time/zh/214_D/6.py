def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    sizes = [1 for i in range(n)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if sizes[x] < sizes[y]:
            x, y = y, x
        parents[y] = x
        sizes[x] += sizes[y]
        return True
    ans = 0
    for u, v, w in edges:
        u, v = u - 1, v - 1
        ans += w * sizes[find(u)] * sizes[find(v)]
        union(u, v)
    print(ans)
