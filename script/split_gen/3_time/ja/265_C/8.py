def main():
    H,W = map(int, input().split())
    G = list()
    for i in range(H):
        G.append(list(input()))
    x,y = 0,0
    while True:
        if G[x][y] == 'R':
            if y == W-1:
                print(-1)
                exit()
            y += 1
        elif G[x][y] == 'L':
            if y == 0:
                print(-1)
                exit()
            y -= 1
        elif G[x][y] == 'U':
            if x == 0:
                print(-1)
                exit()
            x -= 1
        elif G[x][y] == 'D':
            if x == H-1:
                print(-1)
                exit()
            x += 1
        if x == 0 and y == 0:
            print(-1)
            exit()
        if x == H-1 and y == W-1:
            print(x+1,y+1)
            exit()
