def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    x, y = 0, 0
    while True:
        if visited[x][y]:
            print(-1)
            break
        visited[x][y] = True
        if G[x][y] == 'U':
            if x == 0:
                print(x + 1, y + 1)
                break
            else:
                x -= 1
        elif G[x][y] == 'D':
            if x == H - 1:
                print(x + 1, y + 1)
                break
            else:
                x += 1
        elif G[x][y] == 'L':
            if y == 0:
                print(x + 1, y + 1)
                break
            else:
                y -= 1
        elif G[x][y] == 'R':
            if y == W - 1:
                print(x + 1, y + 1)
                break
            else:
                y += 1
