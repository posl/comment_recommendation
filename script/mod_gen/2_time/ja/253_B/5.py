def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                a, b = i, j
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                c, d = i, j
    print(max(abs(a-c), abs(b-d)))

if __name__ == '__main__':
    main()