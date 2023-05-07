def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    ans = 0
    for u in range(N):
        for v in range(u+1, N):
            if v in E[u]:
                continue
            if all(u not in E[v] for v in E[u]):
                ans += 1
    print(ans)
