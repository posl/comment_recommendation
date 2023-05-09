def union_find(n):
    par = list(range(n))
    size = [1] * n
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def same(x, y):
        return root(x) == root(y)
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
    return root, same, unite
n, m = map(int, input().split())
root, same, unite = union_find(n)
for _ in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
print('Yes' if len(set(root(i) for i in range(n))) == 1 else 'No')
