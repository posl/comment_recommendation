def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.append(0)
    a.append(10**18 + 1)
    a.sort()
    for i in range(q):
        l, r = 0, n + 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] - a[m - 1] - 1 < k[i]:
                k[i] -= a[m] - a[m - 1] - 1
                l = m
            else:
                r = m
        print(k[i] + a[l])

if __name__ == '__main__':
    main()