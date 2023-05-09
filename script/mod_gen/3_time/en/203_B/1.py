def main():
    N, K = map(int, input().split())
    print(100 * N * K + 100 * N + 100 * K + N * K)

if __name__ == '__main__':
    main()