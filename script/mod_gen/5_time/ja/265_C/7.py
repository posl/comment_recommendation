def main():
    h, w = map(int, input().split())
    l = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if l[x][y] == "U":
            if x == 0:
                print(x+1, y+1)
                return
            else:
                x -= 1
        elif l[x][y] == "D":
            if x == h-1:
                print(x+1, y+1)
                return
            else:
                x += 1
        elif l[x][y] == "L":
            if y == 0:
                print(x+1, y+1)
                return
            else:
                y -= 1
        elif l[x][y] == "R":
            if y == w-1:
                print(x+1, y+1)
                return
            else:
                y += 1
        if l[x][y] == ".":
            print(x+1, y+1)
            return
        l[x][y] = "."
main()
