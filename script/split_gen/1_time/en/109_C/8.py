def solve():
    N, X = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(X)
    xs.sort()
    ds = [xs[i+1] - xs[i] for i in range(N)]
    d = ds[0]
    for i in range(1, N):
        d = gcd(d, ds[i])
    print(d)
