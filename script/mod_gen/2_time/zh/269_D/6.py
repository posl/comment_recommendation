def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x,y) in black:
        black.remove((x,y))
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x+1,y+1)
N = int(input())
black = set()
for _ in range(N):
    x,y = map(int,input().split())
    black.add((x,y))
ans = 0
while len(black) > 0:
    x,y = black.pop()
    dfs(x,y)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()