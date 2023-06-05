def main():
    a, b, c, d, e, f = map(int, input().split())
    ans = (a * b * c - d * e * f) % 998244353
    print(ans)
