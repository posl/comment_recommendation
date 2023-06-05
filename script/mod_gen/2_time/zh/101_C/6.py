def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    n = N - K
    print(1 + (n + K - 2) // (K - 1))

if __name__ == '__main__':
    main()