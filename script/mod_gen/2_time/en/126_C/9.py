def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - 2) * (K - 1) / (N * N))

if __name__ == '__main__':
    main()