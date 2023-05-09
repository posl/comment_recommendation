def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    x, y = 0, 0
    for _ in range(10**6):
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x < 0 or H-1 < x or y < 0 or W-1 < y:
            print(x+1, y+1)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()