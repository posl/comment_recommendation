def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % pow(10, i+1) < pow(10, i+1) // 2:
            X = X - X % pow(10, i+1)
        else:
            X = X - X % pow(10, i+1) + pow(10, i+1)
    print(X)

if __name__ == '__main__':
    main()