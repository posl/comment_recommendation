def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

if __name__ == '__main__':
    main()