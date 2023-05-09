def dfs(x,y):
    if (x,y) in visited:
        return
    visited.add((x,y))
    if (x-1,y-1) in black:
        dfs(x-1,y-1)
    if (x-1,y) in black:
        dfs(x-1,y)
    if (x,y-1) in black:
        dfs(x,y-1)
    if (x,y+1) in black:
        dfs(x,y+1)
    if (x+1,y) in black:
        dfs(x+1,y)
    if (x+1,y+1) in black:
        dfs(x+1,y+1)
n = int(input())
black = set()
for _ in range(n):
    x,y = map(int,input().split())
    black.add((x,y))
visited = set()
count = 0
for i in black:
    if i not in visited:
        count += 1
        dfs(i[0],i[1])
print(count)

if __name__ == '__main__':
    dfs()