def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    print(" ".join(map(str, X)))

if __name__ == '__main__':
    main()