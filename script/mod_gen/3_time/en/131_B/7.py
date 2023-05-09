def main():
    N, L = map(int, input().split())
    print(N * (2 * L + N - 1) // 2 - L - max(0, L + N - 1))

if __name__ == '__main__':
    main()