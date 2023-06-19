def dfs(v, p, c):
    global color
    color[c].append(v)
    for u in tree[v]:
        if u == p:
            continue
        dfs(u, v, c+1)
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
color = [[] for _ in range(n+1)]
dfs(1, -1, 1)
max_color = max(len(color[i]) for i in range(1, n+1))
print(max_color)
for i in range(1, n+1):
    print(i)
    if len(color[i]) == 0:
        continue
    print(' '.join(map(str, color[i])))

if __name__ == '__main__':
    dfs()