def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    ans = [0]*M
    ans[M-1] = N*(N-1)//2
    uf = UnionFind(N+1)
    for i in range(M-1,0,-1):
        a = AB[i][0]
        b = AB[i][1]
        if uf.same(a,b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - uf.size(a)*uf.size(b)
            uf.union(a,b)
    for i in range(M):
        print(ans[i])
