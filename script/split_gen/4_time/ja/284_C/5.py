def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    v = [0]*n
    def dfs(x):
        v[x] = 1
        for i in g[x]:
            if v[i] == 0:
                dfs(i)
    ans = 0
    for i in range(n):
        if v[i] == 0:
            dfs(i)
            ans += 1
    print(ans)
