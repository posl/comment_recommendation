def main():
    # input
    N, X = map(int, input().split())
    xs = list(map(int, input().split()))
    # compute
    ds = [abs(X-x) for x in xs]
    d = ds[0]
    for i in range(1, N):
        d = gcd(d, ds[i])
    # output
    print(d)
