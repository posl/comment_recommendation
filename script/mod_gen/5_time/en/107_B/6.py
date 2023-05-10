def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    r = []
    c = []
    for i in range(H):
        if a[i].count(".") == W:
            r.append(i)
    for i in range(W):
        if [a[j][i] for j in range(H)].count(".") == H:
            c.append(i)
    for i in range(H):
        if not i in r:
            print("".join([a[i][j] for j in range(W) if not j in c]))

if __name__ == '__main__':
    main()