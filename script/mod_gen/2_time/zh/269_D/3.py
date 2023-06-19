def dfs(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x, y) not in visited:
        visited.add((x, y))
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
n = int(input())
visited = set()
for i in range(n):
    x, y = map(int, input().split())
    dfs(x, y)
print(len(visited))

if __name__ == '__main__':
    dfs()