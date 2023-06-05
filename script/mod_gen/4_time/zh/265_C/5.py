def move(x,y):
    if x<=0 or x>h or y<=0 or y>w:
        return False
    if grid[x-1][y-1] == 'U':
        x -= 1
    elif grid[x-1][y-1] == 'D':
        x += 1
    elif grid[x-1][y-1] == 'L':
        y -= 1
    elif grid[x-1][y-1] == 'R':
        y += 1
    else:
        return False
    return x,y
h,w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
x,y = 1,1
visited = [[0 for i in range(w)] for j in range(h)]
while True:
    if visited[x-1][y-1] == 1:
        print(-1)
        break
    visited[x-1][y-1] = 1
    x,y = move(x,y)
    if x == False:
        print(x,y)
        break

if __name__ == '__main__':
    move()