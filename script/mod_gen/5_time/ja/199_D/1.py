def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True
N, M = map(int, input().split())
G = [[] for _ in range(N)]
color = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = 1
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break
    ans *= 3
print(ans)

if __name__ == '__main__':
    dfs()