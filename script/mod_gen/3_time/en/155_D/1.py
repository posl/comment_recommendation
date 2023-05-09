def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        m = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - (n - i - 1) - 1
                for j in range(i + 1, n):
                    if a[i] * a[j] <= m:
                        cnt += 1
                    else:
                        break
            else:
                for j in range(i + 1, n):
                    if a[i] * a[j] <= m:
                        cnt += 1
                    else:
                        break
        if cnt < k:
            l = m
        else:
            r = m
    print(r)

if __name__ == '__main__':
    main()