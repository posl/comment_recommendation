def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, N+1):
        p[i] += p[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, p[i+K] - p[i])
    print((ans + K) / 2)

if __name__ == '__main__':
    main()