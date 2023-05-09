def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i]-1,b[i]-1)
    ans = 0
    for i in range(n):
        if uf.find(i) == i:
            ans += 1
    print(ans)
