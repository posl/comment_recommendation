def main():
    #input
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    #solve
    # DSU
    par = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def unite(x, y):
        rx = root(x)
        ry = root(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            par[rx] = ry
        else:
            par[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
    def same(x, y):
        return root(x) == root(y)
    # bridge
    ans = [0 for _ in range(M)]
    ans[M-1] = N*(N-1)//2
    for i in range(M-1, 0, -1):
        a, b = AB[i]
        if same(a, b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - (rank[root(a)]+1)*(rank[root(b)]+1)
            unite(a, b)
    #output
    for i in range(M):
        print(ans[i])
