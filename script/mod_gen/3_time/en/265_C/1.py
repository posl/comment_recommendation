def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        else:
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()