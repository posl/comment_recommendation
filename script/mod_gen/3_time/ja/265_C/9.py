def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    #print(H, W)
    #print(G)
    ans = ''
    i = 0
    j = 0
    while True:
        #print(i, j)
        ans += G[i][j]
        if G[i][j] == 'U':
            if i == 0:
                print(-1)
                exit()
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(-1)
                exit()
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(-1)
                exit()
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(-1)
                exit()
            else:
                j += 1
        if ans.count(ans[-1]) >= 3:
            print(-1)
            exit()
        if i == 0 and j == 0:
            print(-1)
            exit()
        if ans[-2:] == 'UD' or ans[-2:] == 'DU' or ans[-2:] == 'LR' or ans[-2:] == 'RL':
            print(-1)
            exit()
        if i == H-1 and j == W-1:
            print(i+1, j+1)
            exit()

if __name__ == '__main__':
    main()