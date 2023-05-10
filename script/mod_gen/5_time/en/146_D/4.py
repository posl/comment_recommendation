def dfs(v, p=-1):
    global k
    global ans
    c = 1
    for u in G[v]:
        if u == p:
            continue
        if c == ans[v]:
            c += 1
        ans[u] = c
        c += 1
        k = max(k, c - 1)
        dfs(u, v)
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = [0] * n
k = 0
dfs(0)
print(k)
for i in range(n - 1):
    print(ans[i])

if __name__ == '__main__':
    dfs()