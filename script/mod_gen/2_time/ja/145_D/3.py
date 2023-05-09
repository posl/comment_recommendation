def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    X -= N
    Y -= N
    if X < 0 or Y < 0:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= (N - i)
        ans %= mod
    for i in range(X):
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    for i in range(Y):
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()