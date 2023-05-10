def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(1, X):
        height += D
    if M < X:
        for i in range(X, N):
            height += D
    print(height)

if __name__ == '__main__':
    main()