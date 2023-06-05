def dfs(v, p, k):
    global ans
    c = 1
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if c == k:
            c += 1
        ans[G[v][i]] = c
        dfs(G[v][i], v, c)
        c += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0] * N
dfs(0, -1, 0)
print(max(ans))
for i in range(N - 1):
    print(ans[i + 1])

if __name__ == '__main__':
    dfs()