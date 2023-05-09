def lcm(a, b):
    from fractions import gcd
    return a * b // gcd(a, b)
a, b = map(int, raw_input().split())
print lcm(a, b)

if __name__ == '__main__':
    lcm()