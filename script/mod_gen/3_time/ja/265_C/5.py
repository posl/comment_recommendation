def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if x == h or x == -1 or y == w or y == -1:
            print(x+1, y+1)
            break
        elif s[x][y] == "R":
            s[x][y] = "."
            y += 1
        elif s[x][y] == "L":
            s[x][y] = "."
            y -= 1
        elif s[x][y] == "U":
            s[x][y] = "."
            x -= 1
        elif s[x][y] == "D":
            s[x][y] = "."
            x += 1
        else:
            print(-1)
            break

if __name__ == '__main__':
    main()