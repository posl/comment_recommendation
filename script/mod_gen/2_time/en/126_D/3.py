def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append((v,w))
        graph[v].append((u,w))
    ans = [None]*N
    ans[0] = 0
    q = [(0,0)]
    while q:
        v, c = q.pop()
        for nv, w in graph[v]:
            if ans[nv] is None:
                ans[nv] = c if w%2 == 0 else 1-c
                q.append((nv,ans[nv]))
    print(*ans,sep='
')
main()
