def main():
    A, B, X = map(int, input().split())
    # X = A * N + B * d(N)
    # N = (X - B * d(N)) / A
    # d(N) = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
    # d(N) = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
    # 10 ** d(N) = 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, ...
    # 10 ** d(N) = 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, ...
    # 10 ** (d(N) - 1) = 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, ...
    # 10 ** (d(N) - 1) = 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, ...
    # 10 ** (d(N) - 1) <= X / A < 10 ** d(N)
    # 1

if __name__ == '__main__':
    main()