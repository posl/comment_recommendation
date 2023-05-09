def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i != 0 and S[i - 1][j] == '.':
                    ans += 1
                if i != H - 1 and S[i + 1][j] == '.':
                    ans += 1
                if j != 0 and S[i][j - 1] == '.':
                    ans += 1
                if j != W - 1 and S[i][j + 1] == '.':
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()