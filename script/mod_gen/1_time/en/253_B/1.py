def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                y1, x1 = i, j
            if S[i][j] == 'o':
                y2, x2 = i, j
    print(max(abs(y1-y2), abs(x1-x2)))

if __name__ == '__main__':
    main()