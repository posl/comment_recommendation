def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, M):
        height += D
    print(height)

if __name__ == '__main__':
    main()