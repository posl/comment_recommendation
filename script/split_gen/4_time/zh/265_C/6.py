def main():
    h,w = map(int,input().split())
    g = [input() for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    x,y = 0,0
    while 0 <= x < h and 0 <= y < w and not visited[x][y]:
        visited[x][y] = 1
        if g[x][y] == "U":
            x -= 1
        elif g[x][y] == "D":
            x += 1
        elif g[x][y] == "L":
            y -= 1
        elif g[x][y] == "R":
            y += 1
    if 0 <= x < h and 0 <= y < w:
        print(x+1,y+1)
    else:
        print(-1)
