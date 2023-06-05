def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if g[x][y] == 'U':
            if x == 0:
                break
            x -= 1
        elif g[x][y] == 'D':
            if x == h - 1:
                break
            x += 1
        elif g[x][y] == 'L':
            if y == 0:
                break
            y -= 1
        elif g[x][y] == 'R':
            if y == w - 1:
                break
            y += 1
    print(x + 1, y + 1)
