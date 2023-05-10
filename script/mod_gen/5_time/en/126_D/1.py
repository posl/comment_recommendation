def dfs(v, c):
    color[v] = c
    for i in range(len(tree[v])):
        if color[tree[v][i][0]] == -1:
            if tree[v][i][1] % 2 == 0:
                dfs(tree[v][i][0], c)
            else:
                dfs(tree[v][i][0], 1-c)
n = int(input())
tree = [[] for i in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))
color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])

if __name__ == '__main__':
    dfs()