def main():
    H, W = map(int, input().split())
    G = [list(input()) for i in range(H)]
    i = 0
    j = 0
    while True:
        if G[i][j] == "U":
            if i == 0:
                print(i + 1, j + 1)
                exit()
            else:
                i -= 1
        elif G[i][j] == "D":
            if i == H - 1:
                print(i + 1, j + 1)
                exit()
            else:
                i += 1
        elif G[i][j] == "L":
            if j == 0:
                print(i + 1, j + 1)
                exit()
            else:
                j -= 1
        elif G[i][j] == "R":
            if j == W - 1:
                print(i + 1, j + 1)
                exit()
            else:
                j += 1
        if i == 0 and j == 0:
            print(-1)
            exit()
