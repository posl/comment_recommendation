def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 0
    for i in range(Y, W):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    print(ans - 3)

if __name__ == '__main__':
    main()