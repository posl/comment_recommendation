def dfs(now,pre,step):
    global ans
    if step > ans:
        return
    if now == 123456789:
        ans = step
        return
    for i in range(4):
        if 0 <= now + dx[i] < 9 and pre != dx[i] and pre != -dx[i]:
            dfs(now + dx[i], -dx[i], step + 1)
dx = [-3,3,-1,1]
ans = 100
start = 0
for i in range(3):
    for j in range(3):
        start += (int(input()) - 1) * 10 ** (8 - (i * 3 + j))
dfs(start,0,0)
print(ans if ans != 100 else -1)

if __name__ == '__main__':
    dfs()