def problems154_d():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(K):
        ans += (p[N-i-1] + 1) / 2
    print(ans)
