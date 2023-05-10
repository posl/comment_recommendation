def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        ans = min(ans, min(abs(l)+r-l, abs(r)+r-l))
    print(ans)
