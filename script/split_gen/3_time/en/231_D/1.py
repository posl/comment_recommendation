def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])
    used = [False] * N
    def dfs(v):
        used[v] = True
        for nv in G[v]:
            if used[nv]:
                continue
            dfs(nv)
    cnt = 0
    for i in range(N):
        if used[i]:
            continue
        dfs(i)
        cnt += 1
    print("Yes" if cnt == 1 else "No")
