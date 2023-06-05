def solve():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(N):
        if len(graph[i])>2:
            print('No')
            return
    print('Yes')
solve()
