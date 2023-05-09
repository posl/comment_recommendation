def main():
    n,q = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    counter = [0]*n
    for _ in range(q):
        p,x = map(int,input().split())
        counter[p-1] += x
    ans = [0]*n
    def dfs(v,p=-1):
        ans[v] = counter[v]
        for to in g[v]:
            if to == p:
                continue
            counter[to] += counter[v]
            dfs(to,v)
    dfs(0)
    print(*ans)

if __name__ == '__main__':
    main()