def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = n
        l = 0
        r = n - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x[i]:
                l = m
            else:
                r = m
        if a[l] >= x[i]:
            ans -= 1
        if a[r] >= x[i]:
            ans -= 1
        print(ans)

if __name__ == '__main__':
    main()