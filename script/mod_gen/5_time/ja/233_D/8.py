def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    a.insert(0, 0)
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    ans = 0
    for i in range(n + 1):
        l = i
        r = n + 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] - a[i] >= k:
                r = m
            else:
                l = m
        if a[r] - a[i] == k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()