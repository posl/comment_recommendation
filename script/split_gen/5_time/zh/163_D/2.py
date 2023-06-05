def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    if k == 1:
        print(n+1)
    else:
        ans = 0
        for i in range(k, n+2):
            ans += i*(n+1-i+1)+1
            ans %= mod
        print(ans)
main()
