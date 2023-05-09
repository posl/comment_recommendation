def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 2^N-1
    ways = pow(2, N, MOD) - 1
    # 2^N-1 - (2^N-1) / gcd(a_1, a_2, ..., a_N)
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
    ways -= pow(2, N, MOD) * pow(gcd, MOD-2, MOD) % MOD
    print(ways % MOD)

if __name__ == '__main__':
    main()