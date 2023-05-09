def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    for i in range(10**6):
        if x == h-1 and y == w-1:
            print(x+1, y+1)
            return
        if g[x][y] == "U":
            if x == 0:
                print(-1)
                return
            x -= 1
        elif g[x][y] == "D":
            if x == h-1:
                print(-1)
                return
            x += 1
        elif g[x][y] == "L":
            if y == 0:
                print(-1)
                return
            y -= 1
        elif g[x][y] == "R":
            if y == w-1:
                print(-1)
                return
            y += 1
    print(-1)
    return

if __name__ == '__main__':
    main()