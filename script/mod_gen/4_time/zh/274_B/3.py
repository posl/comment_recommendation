def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[i][j] = 1
    for i in range(W):
        for j in range(1, H):
            if X[j][i] == 1:
                X[j][i] = X[j-1][i] + 1
    for i in range(H):
        print(*X[i])

if __name__ == '__main__':
    main()