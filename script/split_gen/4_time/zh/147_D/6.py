def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += ((1 << i) % MOD) * (one * zero)
        ans %= MOD
    print(ans)
