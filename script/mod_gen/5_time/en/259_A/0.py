def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(1, X):
        T += D
    for i in range(X, N):
        T += D
    print(T)

if __name__ == '__main__':
    main()