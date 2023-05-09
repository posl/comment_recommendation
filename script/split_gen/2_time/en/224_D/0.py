def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    P = list(map(int, input().split()))
    for i in range(8):
        P[i] -= 1
    P.insert(0, -1)
    P.append(-1)
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if j in G[i]:
                G[i].remove(j)
            else:
                G[i].append(j)
    for i in range(9):
        G[i] = sorted(G[i])
    def dfs(v, p, d, used):
        if v == 8:
            if d == 0:
                return 0
            else:
                return 10**9
        if d == 0:
            return 10**9
        if used[v]:
            return 10**9
        res = 10**9
        used[v] = True
        for u in G[p[v]]:
            res = min(res, dfs(v+1, p, d-1, used))
        used[v] = False
        res = min(res, dfs(v+1, p, d, used))
        return res
    res = dfs(0, P, 16, [False]*9)
    print(-1 if res == 10**9 else res)
