def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        g[x][y] = '.'
        if g[x][y] == 'U':
            if x == 0:
                print(x+1, y+1)
                return
            x -= 1
        elif g[x][y] == 'D':
            if x == h-1:
                print(x+1, y+1)
                return
            x += 1
        elif g[x][y] == 'L':
            if y == 0:
                print(x+1, y+1)
                return
            y -= 1
        elif g[x][y] == 'R':
            if y == w-1:
                print(x+1, y+1)
                return
            y += 1
        else:
            print(x+1, y+1)
            return
        if g[x][y] == '.':
            print(-1)
            return
