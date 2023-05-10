def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    if (x + y) % 3 != 0:
        print(0)
        return
    if (2 * x - y) % 3 != 0:
        print(0)
        return
    if (2 * y - x) % 3 != 0:
        print(0)
        return
    a = (2 * y - x) // 3
    b = (2 * x - y) // 3
    if a < 0 or b < 0:
        print(0)
        return
    n = a + b
    r = min(a, b)
    ans = 1
    for i in range(r):
        ans *= n - i
        ans %= mod
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()