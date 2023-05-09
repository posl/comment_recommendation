def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    def dfs(v,p=-1):
        for nv,w in G[v]:
            if nv==p:
                continue
            dfs(nv,v)
            G[v].append((nv,G[nv][0][1]+w))
    dfs(0)
    ans = 0
    for v in range(N):
        for nv,w in G[v]:
            ans += w
    print(ans)

if __name__ == '__main__':
    main()