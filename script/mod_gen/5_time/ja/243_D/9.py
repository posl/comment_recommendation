def main():
    N, X = map(int, input().split())
    S = input()
    X = bin(X)[2:]
    for s in S:
        if s == 'U':
            X = X[:-1]
        elif s == 'L':
            X = X + '0'
        else:
            X = X + '1'
    print(int(X, 2))

if __name__ == '__main__':
    main()