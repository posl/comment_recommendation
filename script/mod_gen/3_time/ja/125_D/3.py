def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i-1] + a[i] > 0:
            a[i] += a[i-1]
            ans += a[i-1]
        else:
            ans += a[i-1] + a[i]
            a[i] = 0
    print(ans + a[-1])

if __name__ == '__main__':
    main()