def solve():
    n,m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if j in g[i]:
                continue
            for k in range(j+1,n):
                if k in g[i] or k in g[j]:
                    continue
                ans += 1
    print(ans)
