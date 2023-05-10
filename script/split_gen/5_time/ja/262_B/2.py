def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in G[i]:
            for k in G[j]:
                if k in G[i]:
                    ans += 1
    print(ans//6)
