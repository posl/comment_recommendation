def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    k = 1
    for w in g[v]:
        if w == p:
            continue
        while color[k]:
            k += 1
        dfs(w, v, k)
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
ans = [0] * n
color = [False] * (n+1)
dfs(0, -1, 1)
print(max(ans))
for i in range(n-1):
    print(ans[i+1])

if __name__ == '__main__':
    dfs()