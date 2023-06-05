def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()