def main():
    H, W = map(int, input().split())
    G = [list(input()) for i in range(H)]
    x, y = 0, 0
    while True:
        if G[x][y] == 'U':
            if x == 0:
                print(x + 1, y + 1)
                exit()
            x -= 1
        elif G[x][y] == 'D':
            if x == H - 1:
                print(x + 1, y + 1)
                exit()
            x += 1
        elif G[x][y] == 'L':
            if y == 0:
                print(x + 1, y + 1)
                exit()
            y -= 1
        else:
            if y == W - 1:
                print(x + 1, y + 1)
                exit()
            y += 1
main()
