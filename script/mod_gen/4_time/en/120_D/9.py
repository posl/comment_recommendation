def main():
    n,m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.reverse()
    ans = [0]*m
    uf = UnionFind(n)
    ans[0] = n*(n-1)//2
    for i in range(m-1):
        a = ab[i][0]-1
        b = ab[i][1]-1
        if uf.same(a,b):
            ans[i+1] = ans[i]
        else:
            ans[i+1] = ans[i]-uf.size(a)*uf.size(b)
            uf.union(a,b)
    ans.reverse()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()