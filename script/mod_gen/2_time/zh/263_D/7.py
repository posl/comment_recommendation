def solve():
    n,m=map(int,input().split())
    a=[1]*n
    def dfs(i):
        if i==n:
            print(*a)
            return
        for j in range(1,m+1):
            a[i]=j
            dfs(i+1)
    dfs(0)
solve()
