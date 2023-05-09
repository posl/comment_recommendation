def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H - 1):
        for j in range(W - 1):
            if S[i][j] == '#':
                cnt += 1
                S[i][j] = '.'
                S[i + 1][j] = '.' 
                S[i][j + 1] = '.' 
                S[i + 1][j + 1] = '.' 
    print(cnt)

if __name__ == '__main__':
    main()