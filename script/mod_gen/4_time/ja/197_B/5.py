def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 1
    for i in range(Y - 2, -1, -1):
        if S[X - 1][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X - 1][i] == '#':
            break
        ans += 1
    for i in range(X - 2, -1, -1):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()