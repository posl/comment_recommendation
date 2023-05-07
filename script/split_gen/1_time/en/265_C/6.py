def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(input())
    x, y = 0, 0
    for i in range(10**6):
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x < 0 or x >= H or y < 0 or y >= W:
            print(x+1, y+1)
            return
    print(-1)
main()
