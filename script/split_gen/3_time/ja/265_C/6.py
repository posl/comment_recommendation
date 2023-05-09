def main():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    x = 0
    y = 0
    for i in range(1000):
        if x == h-1 and y == w-1:
            break
        if g[x][y] == 'R':
            y += 1
        elif g[x][y] == 'L':
            y -= 1
        elif g[x][y] == 'U':
            x -= 1
        elif g[x][y] == 'D':
            x += 1
        else:
            print(-1)
            return
        if x < 0 or y < 0 or x >= h or y >= w:
            print(-1)
            return
    print(x+1, y+1)
