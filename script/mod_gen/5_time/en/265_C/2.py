def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(input())
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif G[i][j] == 'D':
            if i == H - 1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif G[i][j] == 'R':
            if j == W - 1:
                break
            j += 1
    if i == 0 and j == 0:
        print(-1)
    else:
        print(i+1, j+1)

if __name__ == '__main__':
    main()