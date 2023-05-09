def main():
    a, b, c, d, e, f = map(int, input().split())
    x = a * b * c
    y = d * e * f
    z = x - y
    print(z % 998244353)
