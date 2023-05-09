def lcm(x, y):
    from fractions import gcd
    return (x * y) // gcd(x, y)
