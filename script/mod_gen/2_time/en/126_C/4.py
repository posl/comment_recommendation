def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - K) * (K - 1) * 6 + (N - 1) * 3 + 1)

if __name__ == '__main__':
    main()