def main():
    a, b, c, d, e, f = map(int, input().split())
    mod = 998244353
    print(((a * b * c) - (d * e * f)) % mod)

if __name__ == '__main__':
    main()