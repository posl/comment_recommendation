def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1,10):
        ans += sum(i * 10**j for j in range(18)) * (N // (i * 10**18))
        ans += sum(i * 10**j for j in range(N % (i * 10**18) // i + 1)) % MOD
    print(ans % MOD)
