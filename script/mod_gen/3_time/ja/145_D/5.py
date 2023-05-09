def main():
    import sys
    input = sys.stdin.readline
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    # X + Y = 3N
    # X = N + a, Y = N + b
    # a + b = N
    # a + b = N
    # a = N - b
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y = N - b
    # 2N - b = N
    # b = N
    # X = N - N = 0
    # Y = N - N = 0
    # X + Y = 0
    # N = (X + Y) // 3
    # X = Y = N - N = 0
    # 2N - 0 = N
    # 2N = N
    # N = 2
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y = N - b
    # 2N - b = N
    # b = N
    # X = N - N = 0
    # Y = N - N = 0
    # X + Y = 0
    # N = (X + Y) // 3
    # X = Y = N - N = 0
    # 2N - 0 = N
    # 2N = N
    # N = 1
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y

if __name__ == '__main__':
    main()