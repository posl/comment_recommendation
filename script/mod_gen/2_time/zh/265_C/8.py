def main():
    H, W = map(int, input().split())
    G = [input() for i in range(H)]
    i, j = 0, 0
    while True:
        if G[i][j] == "U":
            if i == 0:
                print(i + 1, j + 1)
                return
            i -= 1
        elif G[i][j] == "D":
            if i == H - 1:
                print(i + 1, j + 1)
                return
            i += 1
        elif G[i][j] == "L":
            if j == 0:
                print(i + 1, j + 1)
                return
            j -= 1
        elif G[i][j] == "R":
            if j == W - 1:
                print(i + 1, j + 1)
                return
            j += 1
        else:
            print(i + 1, j + 1)
            return
        if G[i][j] == ".":
            print(i + 1, j + 1)
            return
        G[i] = G[i][:j] + "." + G[i][j + 1:]
    print(-1)

if __name__ == '__main__':
    main()