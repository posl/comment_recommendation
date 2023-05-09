def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    mod = 10**9 + 7
    X, Y = N - X, N - Y
    ans = 1
    for i in range(1, X + Y + 1):
        ans *= i
        ans %= mod
    for i in range(1, X + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    for i in range(1, Y + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()