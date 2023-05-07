def solve():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    #print(H, W)
    #print(G)
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    x = 0
    y = 0
    while True:
        if G[y][x] == "U":
            if y == 0:
                print(y + 1, x + 1)
                return
            else:
                y -= 1
        elif G[y][x] == "D":
            if y == H - 1:
                print(y + 1, x + 1)
                return
            else:
                y += 1
        elif G[y][x] == "L":
            if x == 0:
                print(y + 1, x + 1)
                return
            else:
                x -= 1
        elif G[y][x] == "R":
            if x == W - 1:
                print(y + 1, x + 1)
                return
            else:
                x += 1
        else:
            print("Invalid Input")
            return
        if visited[y][x]:
            print(-1)
            return
        else:
            visited[y][x] = True

if __name__ == '__main__':
    solve()