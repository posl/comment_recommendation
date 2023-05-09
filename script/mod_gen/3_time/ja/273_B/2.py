def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X + 5 * 10**i) // (10**i * 10) * 10**i * 10
    print(X)

if __name__ == '__main__':
    main()