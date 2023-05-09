def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = [list(a[i]) for i in range(H)]
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                b[i][j] = 1
            else:
                b[i][j] = 0
    c = [0] * W
    d = [0] * H
    for i in range(H):
        if sum(b[i]) == 0:
            d[i] = 1
    for j in range(W):
        for i in range(H):
            if a[i][j] == '#':
                c[j] = 1
    for i in range(H):
        if d[i] == 0:
            for j in range(W):
                if c[j] == 1:
                    print(a[i][j], end='')
            print()

if __name__ == '__main__':
    main()