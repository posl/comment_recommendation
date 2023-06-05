def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (x + y) // 3
    m = x - n
    if m < 0 or m > n:
        print(0)
        return
    ans = 1
    for i in range(m):
        ans *= n - i
        ans %= mod
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()