def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    m = min(X // D, K)
    X -= m * D
    K -= m
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))

if __name__ == '__main__':
    main()