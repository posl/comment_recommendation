def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    m = x-n
    if m < 0:
        print(0)
        return
    def modinv(a, m):
        b, u, v = m, 1, 0
        while b:
            t = a//b
            a -= t*b
            a, b = b, a
            u -= t*v
            u, v = v, u
        u %= m
        if u < 0:
            u += m
        return u
    ans = 1
    for i in range(n):
        ans *= m+i
        ans %= 10**9+7
    for i in range(n):
        ans *= modinv(i+1, 10**9+7)
        ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()