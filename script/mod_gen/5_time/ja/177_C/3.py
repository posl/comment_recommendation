def main():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    s = sum(a)
    for i in range(n):
        s -= a[i]
        ans += a[i]*s
        ans %= MOD
    print(ans)
main()
