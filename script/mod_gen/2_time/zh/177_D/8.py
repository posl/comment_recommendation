def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    sum_a = sum(a)
    for i in range(n-1):
        sum_a -= a[i]
        ans += a[i]*sum_a
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()