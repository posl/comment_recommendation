def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        l = X[i]
        r = X[i + K - 1]
        if l < 0 and r < 0:
            ans = min(ans, -l)
        elif l < 0 and r >= 0:
            ans = min(ans, -l + r + min(-l, r))
        else:
            ans = min(ans, r)
    print(ans)
