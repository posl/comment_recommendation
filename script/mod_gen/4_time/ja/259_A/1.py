def main():
    N, M, X, T, D = map(int, input().split())
    H = T
    for i in range(1, X):
        H -= D
    for i in range(X, M):
        H += D
    print(H)

if __name__ == '__main__':
    main()