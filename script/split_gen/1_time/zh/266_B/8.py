def solve(n):
    if n < 0:
        n = -n
        n = n % 998244353
        n = 998244353 - n
    else:
        n = n % 998244353
    return n
