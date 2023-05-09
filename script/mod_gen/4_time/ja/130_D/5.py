def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(N):
        while r < N and s < K:
            s += a[r]
            r += 1
        if s >= K:
            ans += N - r + 1
        s -= a[l]
    print(ans)

if __name__ == '__main__':
    main()