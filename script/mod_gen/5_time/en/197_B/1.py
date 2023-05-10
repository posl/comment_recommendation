def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()