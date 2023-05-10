def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    if (x + y) % 3 != 0:
        print(0)
        return
    else:
        n = (2 * y - x) // 3
        m = (2 * x - y) // 3
        if n < 0 or m < 0:
            print(0)
            return
        else:
            ans = 1
            for i in range(1, n + 1):
                ans = ans * (m + i) * pow(i, mod - 2, mod) % mod
            print(ans)
main()

if __name__ == '__main__':
    main()