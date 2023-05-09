def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    X = [0 for _ in range(W)]
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

if __name__ == '__main__':
    main()