def main():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].add(v-1)
        G[v-1].add(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if j not in G[i]:
                if i not in G[j]:
                    ans += 1
    print(ans)
