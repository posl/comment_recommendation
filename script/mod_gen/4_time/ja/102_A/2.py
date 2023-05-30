def lcm(a, b):
    from fractions import gcd
    return a * b // gcd(a, b)
n = int(input())
print(lcm(2, n))
