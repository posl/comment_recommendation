def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.reverse()
    uf = UnionFind(n)
    ans = [0]
    for i in range(m-1):
        a = ab[i][0] - 1
        b = ab[i][1] - 1
        if uf.same(a,b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] + uf.size(a) * uf.size(b))
            uf.union(a,b)
    ans.reverse()
    for i in range(m):
        print(ans[i])

if __name__ == '__main__':
    main()