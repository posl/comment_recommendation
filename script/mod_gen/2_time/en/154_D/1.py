def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    ma = s
    for i in range(N-K):
        s = s - p[i] + p[i+K]
        ma = max(ma, s)
    print((ma+K)/2)

if __name__ == '__main__':
    main()