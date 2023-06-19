def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] % m == 0:
            a[i] = a[i] // m
        else:
            a[i] = a[i] // m + 1
    sum = 0
    for i in range(n):
        sum += a[i]
        a[i] = sum
    a.sort()
    cnt = 1
    ans = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()