def main():
    H, W = map(int, input().split())
    C = []
    for h in range(H):
        C.append(input())
    X = [0] * W
    for w in range(W):
        for h in range(H):
            if C[h][w] == '#':
                X[w] += 1
    print(' '.join(map(str, X)))

if __name__ == '__main__':
    main()