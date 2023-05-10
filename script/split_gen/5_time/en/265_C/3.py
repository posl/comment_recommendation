def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1
        else:
            print(i + 1, j + 1)
            return
main()
