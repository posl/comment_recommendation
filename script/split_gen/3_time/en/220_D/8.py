def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 2^N
    two_pow_N = pow(2, N-1, MOD)
    # 10^N
    ten_pow_N = pow(10, N, MOD)
    # 10^(N-1)
    ten_pow_Nminus1 = pow(10, N-1, MOD)
    # 10^(N-2)
    ten_pow_Nminus2 = pow(10, N-2, MOD)
    # 10^(N-3)
    ten_pow_Nminus3 = pow(10, N-3, MOD)
    # 0 - 9 のそれぞれに対して、最終的な値がその数字となる場合の数を求める
    for K in range(10):
        # 10^N - 10^(N-1) * A_1
        ans = (ten_pow_N - ten_pow_Nminus1 * A[0]) % MOD
        # 10^(N-1) - 10^(N-2) * A_2
        ans = (ans - ten_pow_Nminus1 + ten_pow_Nminus2 * A[1]) % MOD
        # 10^(N-2) - 10^(N-3) * A_3
        ans = (ans - ten_pow_Nminus2 + ten_pow_Nminus3 * A[2]) % MOD
        # 10^(N-3) - 10^(N-4) * A_4
        ans = (ans - ten_pow_Nminus3 + ten_pow_Nminus2 * A[3]) % MOD
        # 10^(N-4) - 10^(N-5) * A_5
        ans = (ans - ten_pow_Nminus2 + ten_pow_Nminus1 * A[4]) % MOD
        # 10^(N-5) - 10^(N-6) * A_6
        ans = (ans - ten_pow_Nminus1 + ten_pow_N * A[5]) % MOD
        # 10^(N-6) - 10^(N-7) * A_7
        ans = (ans - ten_pow_N + ten
