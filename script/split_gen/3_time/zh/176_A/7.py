def solve():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x) * t)
    else:
        print(int(n / x) * t + t)
