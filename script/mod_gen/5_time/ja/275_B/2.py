def main():
    A, B, C, D, E, F = map(int, input().split())
    MOD = 998244353
    print(((A * B * C) - (D * E * F)) % MOD)

if __name__ == '__main__':
    main()