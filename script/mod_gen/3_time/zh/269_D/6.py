def dfs(x,y):
    if (x,y) in visited:
        return
    visited.add((x,y))
    for dx,dy in d:
        dfs(x+dx,y+dy)
n = int(input())
d = [(0,-1),(-1,0),(-1,-1),(0,1),(1,0),(1,1)]
visited = set()
for i in range(n):
    x,y = map(int,input().split())
    dfs(x,y)
print(len(visited))

if __name__ == '__main__':
    dfs()