def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X > K * D:
        print(X - K * D)
        return
    K -= X // D
    X %= D
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))

if __name__ == '__main__':
    main()