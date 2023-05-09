def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                a, b = i, j
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                print(max(abs(a-i), abs(b-j)))

if __name__ == '__main__':
    main()