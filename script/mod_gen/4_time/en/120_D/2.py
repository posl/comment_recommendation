def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    ans = [0]*m
    ans[-1] = n*(n-1)//2
    uf = UnionFind(n+1)
    for i in range(m-1,0,-1):
        ans[i-1] = ans[i]
        if uf.root(a[i]) != uf.root(b[i]):
            ans[i-1] -= uf.size(a[i])*uf.size(b[i])
            uf.unite(a[i],b[i])
    print(*ans,sep="\n")

if __name__ == '__main__':
    main()