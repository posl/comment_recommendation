def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    def dfs(v,p):
        for nv,w in G[v]:
            if nv == p:
                continue
            dist[nv] = dist[v] + w
            dfs(nv,v)
    dist = [0]*N
    dfs(0,-1)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += max(dist[i],dist[j])
    print(ans)
