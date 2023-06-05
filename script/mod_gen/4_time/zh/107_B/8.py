def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    #print(a)
    row = [False] * H
    col = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True
    #print(row)
    #print(col)
    for i in range(H):
        if row[i]:
            for j in range(W):
                if col[j]:
                    print(a[i][j], end='')
            print()

if __name__ == '__main__':
    main()