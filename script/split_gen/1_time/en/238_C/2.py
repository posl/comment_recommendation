def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    d = 1
    while d <= N:
        ans += (N // d) * (d - 1) + min(max(N % d - d + 1, 0), d)
        d *= 10
        ans %= MOD
    print(ans)
main()
