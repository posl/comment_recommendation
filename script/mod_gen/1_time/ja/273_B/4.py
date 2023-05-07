def main():
    X, K = map(int, input().split())
    for i in range(K):
        Y = X // 10 ** (i + 1)
        if X % 10 ** (i + 1) >= 5 * 10 ** i:
            Y += 1
        X = Y * 10 ** (i + 1)
    print(X)

if __name__ == '__main__':
    main()