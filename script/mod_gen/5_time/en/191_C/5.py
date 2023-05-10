def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    res = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#" and S[i-1][j] == S[i+1][j] == S[i][j-1] == S[i][j+1] == ".":
                res += 1
    print(res)

if __name__ == '__main__':
    main()