def dfs(i, color):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(3):
        if color[j] == 1:
            continue
        color[j] = 1
        dfs(i + 1, color)
        color[j] = 0
ans = 0
n, m = map(int, input().split())
color = [0] * 3
dfs(0, color)
print(ans)
