def func(h,w,ls):
    max_ = 0
    for i in range(h):
        for j in range(w):
            if ls[i][j] == '#':
                continue
            visited = [[False]*w for _ in range(h)]
            visited[i][j] = True
            stack = [(i,j,0)]
            while stack:
                x,y,cnt = stack.pop()
                max_ = max(max_,cnt)
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= nx < h and 0 <= ny < w and ls[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx,ny,cnt+1))
    return max_
