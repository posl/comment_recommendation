def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == '#':
                ans = 4
                if S[i-1][j] == '#':
                    ans -= 1
                if S[i+1][j] == '#':
                    ans -= 1
                if S[i][j-1] == '#':
                    ans -= 1
                if S[i][j+1] == '#':
                    ans -= 1
    print(ans)
main()

if __name__ == '__main__':
    main()