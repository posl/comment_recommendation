def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    dist = [[-1]*W for i in range(H)]
    q = []
    q.append([0,0])
    dist[0][0] = 0
    while len(q) > 0:
        x,y = q.pop(0)
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H and S[ny][nx] == "." and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append([nx,ny])
    print(dist[H-1][W-1] + 1)

if __name__ == '__main__':
    main()