def dfs(x, y):
    if (x, y) in black:
        black.remove((x, y))
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
n = int(input())
black = set()
for i in range(n):
    x, y = map(int, input().split())
    black.add((x, y))
ans = 0
while black:
    x, y = black.pop()
    ans += 1
    dfs(x, y)
print(ans)
