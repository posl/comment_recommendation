def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    #print(H, W)
    #print(G)
    
    # 0:上 1:右 2:下 3:左
    # dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    # 0:右 1:下 2:左 3:上
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    # 0:右 1:下 2:左 3:上
    d = 0
    x, y = 0, 0
    for i in range(10000000):
        #print(x, y)
        if x == W-1 and y == H-1:
            print(y+1, x+1)
            return
        if G[y][x] == "U":
            d = 3
        elif G[y][x] == "D":
            d = 1
        elif G[y][x] == "L":
            d = 2
        elif G[y][x] == "R":
            d = 0
        else:
            print("error")
            return
        x = x + dx[d]
        y = y + dy[d]
        if x < 0 or x >= W or y < 0 or y >= H:
            print(-1)
            return
    print(-1)
    return
