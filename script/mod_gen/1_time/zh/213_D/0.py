def dfs(x, pre):
    global ans
    ans.append(x)
    for i in range(len(g[x])):
        if g[x][i] == pre:
            continue
        dfs(g[x][i], x)
        ans.append(x)
n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n+1):
    g[i].sort()
ans = []
dfs(1, -1)
print(*ans)

if __name__ == '__main__':
    dfs()