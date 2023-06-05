def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    s = sum(a) % mod
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= mod
    print(ans)
