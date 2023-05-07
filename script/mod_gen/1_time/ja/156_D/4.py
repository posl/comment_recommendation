def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7
    ans = pow(2, N, MOD) - 1
    ans -= comb(N, A, MOD)
    ans -= comb(N, B, MOD)
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()