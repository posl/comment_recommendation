def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = pow(2, n, mod) - pow(2, n - 1, mod)
    print(ans % mod)
