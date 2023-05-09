def main():
    # input
    a, b, c, d, e, f = map(int, input().split())
    # compute
    x = (a * b * c) % 998244353
    y = (d * e * f) % 998244353
    # output
    print((x - y) % 998244353)

if __name__ == '__main__':
    main()