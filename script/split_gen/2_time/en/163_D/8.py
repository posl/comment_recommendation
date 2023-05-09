def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    def sum_of_arithmetic_series(first, last, n):
        return (first + last) * n // 2
    ans = 0
    for i in range(K, N + 2):
        ans += sum_of_arithmetic_series(10 ** 100, 10 ** 100 + i - 1, i) - sum_of_arithmetic_series(10 ** 100, 10 ** 100 + N - i, N - i + 1) + 1
        ans %= MOD
    print(ans)
