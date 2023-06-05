def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7
    t = pow(2, N, MOD) - 1
    c = 1
    for i in range(N, N - A, -1):
        c = c * i % MOD
    for i in range(1, A + 1):
        c = c * pow(i, MOD - 2, MOD) % MOD
    t -= c
    c = 1
    for i in range(N, N - B, -1):
        c = c * i % MOD
    for i in range(1, B + 1):
        c = c * pow(i, MOD - 2, MOD) % MOD
    t -= c
    print((t % MOD + MOD) % MOD)

if __name__ == '__main__':
    main()