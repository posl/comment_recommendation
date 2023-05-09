def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    #print(G)
    #print(N)
    #print(G)
    #print(DFS(0,G))
    ans = 0
    for i in range(N):
        ans += DFS(i,G)[0]
    print(ans)
