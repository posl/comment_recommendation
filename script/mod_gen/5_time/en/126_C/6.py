def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1.0)
    else:
        n = N
        p = 1
        while n < K:
            n *= 2
            p /= 2
        print((N*p + (n-K+1)*p*2)/N)

if __name__ == '__main__':
    main()