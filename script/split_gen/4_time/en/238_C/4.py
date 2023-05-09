def f(n):
    if n < 10:
        return n
    else:
        d = len(str(n))
        return (n - 10**(d-1) + 1) * d + (9 * (10**(d-1) - 1) // 2) * d + 45 * (d - 1) * (10**(d-2)) + 9 * f(10**(d-1) - 1)
N = int(input())
print(f(N) % 998244353)
