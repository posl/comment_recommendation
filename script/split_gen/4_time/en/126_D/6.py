def main():
    import sys
    sys.setrecursionlimit(10**6)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [0]*N
    def dfs(v,p):
        for nv,w in G[v]:
            if nv == p:
                continue
            ans[nv] = ans[v] + w%2
            dfs(nv,v)
    dfs(0,-1)
    ans = [str(a%2) for a in ans]
    print('
'.join(ans))
main()
