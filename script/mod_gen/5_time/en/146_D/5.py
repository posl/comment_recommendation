def dfs(u, p, c):
    global ans
    ans = max(ans, c)
    k = 1
    for v in G[u]:
        if v == p:
            continue
        if k == c:
            k += 1
        print(k)
        dfs(v, u, k)
        k += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)
ans = 0
dfs(0, -1, 0)
print(ans)

if __name__ == '__main__':
    dfs()