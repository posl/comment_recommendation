def solve():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2], reverse=True)
    parents = [i for i in range(n+1)]
    ranks = [0 for i in range(n+1)]
    def find(x):
        if parents[x] == x:
            return x
        else:
            return find(parents[x])
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return False
        if ranks[x_root] > ranks[y_root]:
            parents[y_root] = x_root
        elif ranks[y_root] > ranks[x_root]:
            parents[x_root] = y_root
        else:
            parents[y_root] = x_root
            ranks[x_root] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    num = [1 for i in range(n+1)]
    res = 0
    for u, v, w in edges:
        res += w * num[find(u)] * num[find(v)]
        union(u, v)
        num[find(u)] += num[find(v)]
    print(res)
