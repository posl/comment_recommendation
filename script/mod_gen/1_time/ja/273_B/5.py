def main():
    X, K = map(int, input().split())
    for i in range(K):
        Y = X // (10 ** i) * (10 ** i) + (10 ** i) // 2
        if Y % (10 ** (i + 1)) == 0:
            X = Y // (10 ** (i + 1)) * (10 ** (i + 1))
        else:
            X = Y // (10 ** (i + 1)) * (10 ** (i + 1)) + (10 ** (i + 1))
    print(X)

if __name__ == '__main__':
    main()