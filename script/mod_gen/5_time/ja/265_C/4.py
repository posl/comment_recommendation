def solve():
    H,W = map(int,input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x = 0
    y = 0
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x < 0 or H <= x or y < 0 or W <= y:
            print(x+1,y+1)
            return
        if visited[x][y]:
            print(-1)
            return
        visited[x][y] = True

if __name__ == '__main__':
    solve()