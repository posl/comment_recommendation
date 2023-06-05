def main():
    H,W = map(int,input().split())
    G = []
    for i in range(H):
        G.append(input())
    x,y = 0,0
    for i in range(H*W):
        if G[x][y] == 'U':
            if x != 0:
                x -= 1
            else:
                print(-1)
                return
        elif G[x][y] == 'D':
            if x != H-1:
                x += 1
            else:
                print(-1)
                return
        elif G[x][y] == 'L':
            if y != 0:
                y -= 1
            else:
                print(-1)
                return
        elif G[x][y] == 'R':
            if y != W-1:
                y += 1
            else:
                print(-1)
                return
    print(x+1,y+1)

if __name__ == '__main__':
    main()