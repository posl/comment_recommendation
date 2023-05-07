def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x, y = i, j
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                ans = max(ans, abs(x - i) + abs(y - j))
    print(ans)

if __name__ == '__main__':
    main()