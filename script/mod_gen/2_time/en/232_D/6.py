def solve():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    q = [(0,0)]
    visited[0][0] = True
    while q:
        x,y = q.pop(0)
        for dx,dy in [(0,1),(1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and c[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
    return sum([sum(row) for row in visited])
print(solve())
