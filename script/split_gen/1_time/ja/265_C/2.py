def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    x = 0
    y = 0
    for i in range(10**6):
        if x == H-1 and y == W-1:
            print(x+1, y+1)
            return
        if G[x][y] == 'U' and x != 0:
            x -= 1
        elif G[x][y] == 'D' and x != H-1:
            x += 1
        elif G[x][y] == 'L' and y != 0:
            y -= 1
        elif G[x][y] == 'R' and y != W-1:
            y += 1
        else:
            print(-1)
            return
    print(-1)
