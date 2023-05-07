def main():
    H, W = map(int, input().split())
    X = [0] * W
    for i in range(H):
        line = input()
        for j in range(W):
            if line[j] == '#':
                X[j] += 1
    print(*X)

if __name__ == '__main__':
    main()