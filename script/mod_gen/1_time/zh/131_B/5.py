def main():
    N, L = map(int, input().split())
    print((2 * L + N - 1) * N // 2 - L * N)

if __name__ == '__main__':
    main()