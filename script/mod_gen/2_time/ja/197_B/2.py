def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(X-1, 0, -1):
        if S[i-1][Y-1] == '#':
            break
        ans += 1
    for i in range(X-1, H):
        if S[i+1][Y-1] == '#':
            break
        ans += 1
    for i in range(Y-1, 0, -1):
        if S[X-1][i-1] == '#':
            break
        ans += 1
    for i in range(Y-1, W):
        if S[X-1][i+1] == '#':
            break
        ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()