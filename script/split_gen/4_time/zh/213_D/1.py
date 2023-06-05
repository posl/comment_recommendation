def dfs(now, pre):
    print(now, end=" ")
    for i in range(len(tree[now])):
        if tree[now][i] != pre:
            dfs(tree[now][i], now)
            print(now, end=" ")
n = int(input())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
dfs(0, -1)
