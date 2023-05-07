def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                start = [i,j]
            elif S[i][j] == 'x':
                goal = [i,j]
    queue = [[start[0],start[1],0]]
    visited = [[0 for i in range(W)] for j in range(H)]
    visited[start[0]][start[1]] = 1
    while queue:
        x,y,cnt = queue.pop(0)
        if [x,y] == goal:
            print(cnt)
            exit()
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx,ny,cnt+1])

if __name__ == '__main__':
    main()