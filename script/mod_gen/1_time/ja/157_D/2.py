def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print('No')
            exit()
print('Yes')

if __name__ == '__main__':
    dfs()