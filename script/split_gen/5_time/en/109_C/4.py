def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1] - x[i] for i in range(N)]
    import functools
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    print(functools.reduce(gcd, d))
