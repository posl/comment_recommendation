def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    minus = 0
    for i in range(n-1):
        if a[i] < 0:
            minus += 1
        if minus % 2 == 0:
            ans += abs(a[i])
        else:
            ans -= abs(a[i])
        a[i+1] += a[i]
    if minus % 2 == 0:
        ans += a[-1]
    else:
        ans -= a[-1]
    print(ans)

if __name__ == '__main__':
    main()