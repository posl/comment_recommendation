def solve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l <= 0 <= r:
            ans = min(ans, min(-l, r) * 2 + max(-l, r))
        else:
            ans = min(ans, max(-l, r))
    print(ans)
