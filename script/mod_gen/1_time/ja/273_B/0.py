def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = X // (10 ** i) * (10 ** i) + round((X % (10 ** i)) / (10 ** i)) * (10 ** i)
    print(X)

if __name__ == '__main__':
    main()