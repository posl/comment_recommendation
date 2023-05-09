def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        if a[i-1] > 0:
            ans += a[i-1]
            a[i-1] = 0
        if a[i] < 0:
            ans += a[i]
            a[i] = 0
    if a[n-1] > 0:
        ans += a[n-1]
        a[n-1] = 0
    print(ans)

if __name__ == '__main__':
    main()