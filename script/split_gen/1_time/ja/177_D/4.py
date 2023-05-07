def main():
    n,m = map(int,input().split())
    f = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        f[a-1].add(b-1)
        f[b-1].add(a-1)
    ans = 0
    uf = UnionFind(n)
    for i in range(n):
        for j in f[i]:
            uf.union(i,j)
    ans = uf.size()
    print(ans)
