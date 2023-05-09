def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i]*s
    print(ans%mod)

if __name__ == '__main__':
    main()