def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if not (x,y) in d:
        return
    if d[(x,y)]:
        return
    d[(x,y)] = True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n = int(input())
d = {}
for i in range(n):
    x,y = map(int,input().split())
    d[(x,y)] = False
ans = 0
for i in range(n):
    x,y = map(int,input().split())
    if d[(x,y)]:
        continue
    ans += 1
    dfs(x,y)
print(ans)
