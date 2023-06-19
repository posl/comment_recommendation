def solve():
    N,M = map(int,input().split())
    edges = []
    for i in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                cnt = 0
                for edge in edges:
                    if edge[0] == i and edge[1] == j:
                        cnt += 1
                ans += cnt * (cnt - 1) // 2
    print(ans)
