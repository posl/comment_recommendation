def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    nCa = 1
    nCb = 1
    for i in range(b):
        nCa = nCa * (n - i) % mod
        nCb = nCb * (i + 1) % mod
    ans -= nCa * pow(nCb, mod - 2, mod) % mod
    nCa = 1
    nCb = 1
    for i in range(a):
        nCa = nCa * (n - i) % mod
        nCb = nCb * (i + 1) % mod
    ans -= nCa * pow(nCb, mod - 2, mod) % mod
    print(ans % mod)

if __name__ == '__main__':
    main()