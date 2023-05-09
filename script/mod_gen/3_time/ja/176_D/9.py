def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [input() for _ in range(H)]
    #壁の場合は-1を代入
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '-1' + S[i][j+1:]
    S = [list(map(int,s.split())) for s in S]
    #初期化
    que = deque()
    for i in range(H):
        for j in range(W):
            if i == Ch-1 and j == Cw-1:
                S[i][j] = 0
                que.append((i,j))
            else:
                S[i][j] = -1
    #bfs
    while que:
        y,x = que.popleft()
        #移動A
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= y+i < H and 0 <= x+j < W:
                if S[y+i][x+j] == -1:
                    S[y+i][x+j] = S[y][x]
                    que.appendleft((y+i,x+j))
        #移動B
        for i,j in ((-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
                    (-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),
                    (0,-2),(0,-1),(0,0),(0,1),(0,2),
                    (1,-2),(1,-1),(1,0),(1,1),(1,2),
                    (2,-2),(2,-1),(2,0),(2,1),(2,2)):
            if 0 <= y+i < H and 0 <= x+j < W:
                if S[y+i][x+j] == -1:
                    S[y+i][x+j] = S[y][x] + 1
                    que.append((y+i,x+j))
    #print(S

if __name__ == '__main__':
    main()