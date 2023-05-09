def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    ans = 1
    for i in range(2, int(M**0.5)+1):
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                M //= i
                cnt += 1
            tmp = pow(i, cnt*N, MOD)
            ans *= (tmp-1) * pow(i-1, MOD-2, MOD) % MOD
            ans %= MOD
    if M != 1:
        ans *= (pow(M, N, MOD)-1) * pow(M-1, MOD-2, MOD) % MOD
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()