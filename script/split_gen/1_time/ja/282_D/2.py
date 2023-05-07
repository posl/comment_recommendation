def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if j not in G[i]:
                if (len(G[i])+len(G[j]))%2==0:
                    ans += 1
    print(ans)
