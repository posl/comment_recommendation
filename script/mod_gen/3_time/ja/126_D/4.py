def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u].append((v,w))
        G[v].append((u,w))
    ans = [0] * (N+1)
    def dfs(s,p):
        for t,w in G[s]:
            if t == p: continue
            ans[t] = ans[s] ^ (w%2)
            dfs(t,s)
    dfs(1,-1)
    for i in range(1,N+1):
        print(ans[i])

if __name__ == '__main__':
    main()