def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        for i in range(M, X):
            T += D
    else:
        for i in range(X, M):
            T -= D
    print(T)

if __name__ == '__main__':
    main()