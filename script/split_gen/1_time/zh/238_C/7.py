def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 10):
        x = i
        while x <= N:
            y = min(N, x * 10 - 1)
            ans += (y - x + 1) * i
            x *= 10
    print(ans % MOD)
