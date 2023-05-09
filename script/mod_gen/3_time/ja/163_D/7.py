def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    a = [0] * (n+2)
    b = [0] * (n+2)
    a[0] = 1
    b[0] = 1
    for i in range(1, n+2):
        a[i] = (a[i-1] * i) % mod
        b[i] = pow(a[i], mod-2, mod)
    ans = 0
    for i in range(k):
        ans += a[n+1] * b[i] * b[n+1-i] % mod
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()