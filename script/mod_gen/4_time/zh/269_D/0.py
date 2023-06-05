def dfs(x,y):
    if not (x,y) in s:
        return
    s.remove((x,y))
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n = int(input())
s = set()
for i in range(n):
    x,y = map(int,input().split())
    s.add((x,y))
ans = 0
while len(s)>0:
    x,y = s.pop()
    dfs(x,y)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()