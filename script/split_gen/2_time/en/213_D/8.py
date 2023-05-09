def main():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N-1)]
    AB = [[a-1,b-1] for a,b in AB]
    AB.sort(key=lambda x:x[0])
    G = [[] for _ in range(N)]
    for a,b in AB:
        G[a].append(b)
        G[b].append(a)
    ans = []
    def dfs(v,p):
        ans.append(v+1)
        for nv in G[v]:
            if nv==p:
                continue
            dfs(nv,v)
            ans.append(v+1)
    dfs(0,-1)
    print(*ans)
