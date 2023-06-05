def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    pos = [0, 0]
    while True:
        if g[pos[0]][pos[1]] == "U":
            if pos[0] == 0:
                print(pos[0] + 1, pos[1] + 1)
                break
            else:
                pos[0] -= 1
        elif g[pos[0]][pos[1]] == "D":
            if pos[0] == h - 1:
                print(pos[0] + 1, pos[1] + 1)
                break
            else:
                pos[0] += 1
        elif g[pos[0]][pos[1]] == "L":
            if pos[1] == 0:
                print(pos[0] + 1, pos[1] + 1)
                break
            else:
                pos[1] -= 1
        elif g[pos[0]][pos[1]] == "R":
            if pos[1] == w - 1:
                print(pos[0] + 1, pos[1] + 1)
                break
            else:
                pos[1] += 1
    else:
        print(-1)

if __name__ == '__main__':
    main()