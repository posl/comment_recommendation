def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(H)]
    b = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j == W-1:
                    if i == H-1:
                        pass
                    else:
                        b.append([i+1, j+1, i+2, j+1])
                        a[i+1][j] += 1
                else:
                    b.append([i+1, j+1, i+1, j+2])
                    a[i][j+1] += 1
    print(len(b))
    for i in range(len(b)):
        print(b[i][0], b[i][1], b[i][2], b[i][3])

if __name__ == '__main__':
    main()