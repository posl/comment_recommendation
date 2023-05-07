def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        cnt += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        cnt += 1
    for j in range(Y-2, -1, -1):
        if S[X-1][j] == '#':
            break
        cnt += 1
    for j in range(Y, W):
        if S[X-1][j] == '#':
            break
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()