def dfs(node, parent, color, color_used):
    color_used[color] = True
    k = 1
    for child in node:
        if child != parent:
            while color_used[k]:
                k += 1
            print(k)
            dfs(node, node.index(child), k, color_used)
n = int(input())
node = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)
print(node)
color_used = [False] * (n+1)
print(1)
dfs(node, 0, 1, color_used)
