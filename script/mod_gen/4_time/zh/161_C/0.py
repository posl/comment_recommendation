def main():
    N, K = map(int, input().split())
    while True:
        if N < K:
            break
        N = N % K
    if N > K/2:
        N = K - N
    print(N)

if __name__ == '__main__':
    main()