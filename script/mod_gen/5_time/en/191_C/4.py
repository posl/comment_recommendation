def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                if S[i-1][j] == "." or S[i+1][j] == "." or S[i][j-1] == "." or S[i][j+1] == ".":
                    ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()