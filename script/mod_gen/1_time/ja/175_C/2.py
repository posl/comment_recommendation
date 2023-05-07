def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if K * D <= X:
        print(X - K * D)
    else:
        K -= X // D
        X %= D
        if K % 2 == 0:
            print(X)
        else:
            print(D - X)

if __name__ == '__main__':
    main()