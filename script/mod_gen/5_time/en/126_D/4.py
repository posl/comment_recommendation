def dfs(v, c):
    color[v] = c
    for u, w in tree[v]:
        if color[u] == -1:
            dfs(u, c ^ w % 2)
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    tree[u - 1].append((v - 1, w))
    tree[v - 1].append((u - 1, w))
color = [-1] * N
dfs(0, 0)
print(*color, sep='\n')

if __name__ == '__main__':
    dfs()