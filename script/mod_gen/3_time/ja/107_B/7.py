def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    #print(H, W)
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    for i in range(H):
        if a[i] == '.' * W:
            continue
        else:
            for j in range(W):
                if a[i][j] == '#':
                    break
                else:
                    print(a[i][j], end='')
            print()
    #print(a[0][0], a[0][1], a[0][2], a[0][3])
    #print(a[1][0], a[1][1], a[1][2], a[1][3])
    #print(a[2][0], a[2][1], a[2][2], a[2][3])

if __name__ == '__main__':
    main()