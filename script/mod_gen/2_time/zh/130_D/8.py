def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K)
    #print(a)
    #累積和を求める
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + a[i]
    #print(s)
    #しゃくとり法
    ans = 0
    r = 0
    for l in range(N):
        while r < N+1 and s[r] - s[l] < K:
            r += 1
        ans += N - r + 1
    print(ans)

if __name__ == '__main__':
    main()