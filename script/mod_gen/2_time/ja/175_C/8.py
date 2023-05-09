def main():
    # input
    X, K, D = map(int, input().split())
    # compute
    X = abs(X)
    if X <= K*D:
        K -= X//D
        X %= D
        if K%2 == 1:
            X = abs(X-D)
    # output
    print(X)

if __name__ == '__main__':
    main()