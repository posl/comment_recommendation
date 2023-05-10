def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j]
        if sum % n == 0:
            ans += 1
    print(ans % mod)

if __name__ == '__main__':
    main()