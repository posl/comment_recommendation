def solve():
    n,m = map(int,input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    ans = 0
    for i in range(n):
        for j in edge[i]:
            for k in edge[j]:
                if k in edge[i]:
                    ans += 1
    print(ans//6)
