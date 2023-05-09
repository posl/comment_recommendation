def main():
    n, q = map(int, input().split())
    par = [i for i in range(n+1)]
    rank = [0 for i in range(n+1)]
    size = [1 for i in range(n+1)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    def getsize(x):
        return size[find(x)]
    for i in range(q):
        c, x, y = map(int, input().split())
        if c == 1:
            unite(x, y)
        elif c == 2:
            unite(x, y)
        else:
            print(getsize(x), end = " ")
            for j in range(1, n+1):
                if same(x, j):
                    print(j, end = " ")
            print()
