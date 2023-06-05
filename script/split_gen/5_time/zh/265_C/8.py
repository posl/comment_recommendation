def main():
    H,W = map(int,input().split())
    G = [[0 for i in range(W+2)] for j in range(H+2)]
    for i in range(1,H+1):
        G[i] = [0] + list(input()) + [0]
    x = 1
    y = 1
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x == 0 or x == H+1 or y == 0 or y == W+1:
            break
    if x == 0:
        x += 1
    elif x == H+1:
        x -= 1
    elif y == 0:
        y += 1
    elif y == W+1:
        y -= 1
    print(x,y)
