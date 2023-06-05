def dfs(i, j, k):
    global ans
    if i == N:
        ans += 1
        return
    if j == 3:
        dfs(i+1, 0, k)
        return
    if k & (1 << j):
        dfs(i, j+1, k)
        return
    for x in G[i]:
        if k & (1 << C[x]):
            dfs(i, j+1, k)
            return
    C[i] = j
    dfs(i, j+1, k | (1 << j))
    C[i] = -1
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
C = [-1] * N
ans = 0
dfs(0, 0, 0)
print(ans)

if __name__ == '__main__':
    dfs()