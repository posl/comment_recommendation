def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                if S[i-1][j] == "." and S[i+1][j] == "." and S[i][j-1] == "." and S[i][j+1] == ".":
                    ans = 1
                    break
        if ans == 1:
            break
    if ans == 1:
        print(4)
    else:
        print(2)

if __name__ == '__main__':
    main()