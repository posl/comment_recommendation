def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    if ans == H + W - 1:
        print(1)
    elif ans == H + W - 2:
        print(2)
    elif ans == H + W:
        print(4)
    else:
        print(0)

if __name__ == '__main__':
    main()