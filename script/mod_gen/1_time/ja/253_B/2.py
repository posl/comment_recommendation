def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x = i
                y = j
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                ans = max(ans, abs(i - x) + abs(j - y))
    print(ans)

if __name__ == '__main__':
    main()