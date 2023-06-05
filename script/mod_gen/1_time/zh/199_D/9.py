def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        if color[edge[v][i]] == c:
            return False
        if color[edge[v][i]] == 0 and not dfs(edge[v][i], -c):
            return False
    return True
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
color = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
        else:
            ans = 0
            break
print(3 ** ans)

if __name__ == '__main__':
    dfs()