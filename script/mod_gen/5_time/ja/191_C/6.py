def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i][j - 1] == '.' and S[i + 1][j] == '.' and S[i][j + 1] == '.':
                ans += 1
    if ans == 0:
        print(1)
    else:
        print(ans)

if __name__ == '__main__':
    main()