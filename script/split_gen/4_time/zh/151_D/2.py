def dfs(i,j):
    global ans
    ans = max(ans,cnt[i][j])
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.' and cnt[ni][nj] == 0:
            cnt[ni][nj] = cnt[i][j] + 1
            dfs(ni,nj)
            cnt[ni][nj] = 0
h,w = map(int,input().split())
s = [input() for _ in range(h)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = [[0]*w for _ in range(h)]
            cnt[i][j] = 1
            dfs(i,j)
print(ans-1)
