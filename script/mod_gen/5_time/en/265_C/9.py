def main():
    # Write code here
    H,W = map(int,input().split())
    G = [list(input()) for i in range(H)]
    x,y = 0,0
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        else:
            y += 1
        if x < 0 or x >= H or y < 0 or y >= W:
            print(x+1,y+1)
            break

if __name__ == '__main__':
    main()