def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * a[i]
        ans %= mod
    ans *= n * (n-1) // 2
    ans %= mod
    print(ans)
