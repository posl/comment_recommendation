def main():
    A, B, X = map(int, input().split())
    # 1 <= N <= 10^9
    # 1 <= X <= 10^18
    # A * N + B * d(N) <= X
    # d(N) = len(str(N))
    # A * N + B * len(str(N)) <= X
    # A * N <= X - B * len(str(N))
    # N <= (X - B * len(str(N))) / A

if __name__ == '__main__':
    main()