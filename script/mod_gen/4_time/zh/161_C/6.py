def main():
    N, K = map(int, input().split())
    while N >= K:
        N = N - K
    if N < K:
        if N < K - N:
            print(N)
        else:
            print(K - N)

if __name__ == '__main__':
    main()