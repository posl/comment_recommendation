def main():
    H, W = map(int, input().split())
    X = [0] * W
    for _ in range(H):
        for i, c in enumerate(input()):
            if c == '#':
                X[i] += 1
    print(*X)

if __name__ == '__main__':
    main()