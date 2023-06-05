def main():
    N, M = map(int, input().split())
    # 邻接矩阵
    adj = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        adj[A - 1][B - 1] = C
    # Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    # 计算f(s, t, k)
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if s != t and t != k and k != s:
                    ans += adj[s][t] + adj[t][k]
    print(ans)
