def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append((v,w))
        G[v].append((u,w))
    color = [0] * N
    def dfs(u,p,c):
        color[u] = c
        for v,w in G[u]:
            if v == p:
                continue
            if w % 2 == 0:
                dfs(v,u,c)
            else:
                dfs(v,u,1-c)
    dfs(0,-1,0)
    for i in range(N):
        print(color[i])

if __name__ == '__main__':
    main()