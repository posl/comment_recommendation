def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if N == 1:
        print(x[0] - X)
        return
    ans = x[1] - x[0]
    for i in range(2, N):
        ans = gcd(ans, x[i] - x[i - 1])
    print(ans)
