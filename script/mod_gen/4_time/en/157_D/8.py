def dfs(x, y):
    if x in visited:
        return
    visited.add(x)
    if x in friend:
        for z in friend[x]:
            if z == y:
                continue
            dfs(z, y)
    if x in block:
        for z in block[x]:
            if z == y:
                continue
            dfs(z, y)
N, M, K = map(int, input().split())
friend = {}
block = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in friend:
        friend[a] = set()
    friend[a].add(b)
    if b not in friend:
        friend[b] = set()
    friend[b].add(a)
for _ in range(K):
    c, d = map(int, input().split())
    if c not in block:
        block[c] = set()
    block[c].add(d)
    if d not in block:
        block[d] = set()
    block[d].add(c)
ans = [0] * N
for i in range(1, N + 1):
    visited = set()
    for j in range(1, N + 1):
        if i == j:
            continue
        dfs(j, i)
    ans[i - 1] = N - len(visited) - 1
print(*ans)

if __name__ == '__main__':
    dfs()