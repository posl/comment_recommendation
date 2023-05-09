def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i, j = 0, 0
    while (i, j) != (H - 1, W - 1):
        if G[i][j] == 'R':
            G[i][j] = '.'
            j += 1
            if j >= W:
                print(-1)
                return
        elif G[i][j] == 'D':
            G[i][j] = '.'
            i += 1
            if i >= H:
                print(-1)
                return
        elif G[i][j] == 'L':
            G[i][j] = '.'
            j -= 1
            if j < 0:
                print(-1)
                return
        elif G[i][j] == 'U':
            G[i][j] = '.'
            i -= 1
            if i < 0:
                print(-1)
                return
        else:
            print(-1)
            return
    print(i + 1, j + 1)

if __name__ == '__main__':
    main()