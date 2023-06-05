def dfs(node, color, visited, tree, ans):
    visited[node] = True
    ans[node] = color
    for i in tree[node]:
        if visited[i] == False:
            if color == 0:
                dfs(i, 1, visited, tree, ans)
            else:
                dfs(i, 0, visited, tree, ans)
n = int(input())
tree = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)
visited = [False] * n
ans = [0] * n
dfs(0, 0, visited, tree, ans)
for i in ans:
    print(i)

if __name__ == '__main__':
    dfs()