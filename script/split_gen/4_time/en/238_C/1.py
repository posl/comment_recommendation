def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 19):
        a = N // 10**i
        b = N % 10**i
        ans += a * 45 * 10**(i-1) * i
        ans %= MOD
        ans += b * i
        ans %= MOD
        ans += (b+1) * (b+2) // 2
        ans %= MOD
    print(ans)
