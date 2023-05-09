def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 200
    d = {0: 1}
    ans = 0
    for i in range(n):
        a[i] = a[i] % mod
        if i > 0:
            a[i] += a[i-1]
        a[i] %= mod
        if a[i] in d:
            ans += d[a[i]]
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    print(ans)

if __name__ == '__main__':
    main()