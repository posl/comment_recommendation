def main():
    H,W = map(int,input().split())
    G = [list(input()) for i in range(H)]
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i != 0:
                i -= 1
            else:
                break
        elif G[i][j] == 'D':
            if i != H-1:
                i += 1
            else:
                break
        elif G[i][j] == 'L':
            if j != 0:
                j -= 1
            else:
                break
        elif G[i][j] == 'R':
            if j != W-1:
                j += 1
            else:
                break
        else:
            break
    if G[i][j] == '.':
        print(i+1,j+1)
    else:
        print(-1)

if __name__ == '__main__':
    main()