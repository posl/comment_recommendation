def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    answer = 0
    for i in range(N):
        for v in G[i]:
            for w in G[v]:
                if w in G[i]:
                    answer += 1
    print(answer // 6)
