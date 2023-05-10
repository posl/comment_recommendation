def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)
a, b = map(int, input().split())
print(lcm(a, b))
