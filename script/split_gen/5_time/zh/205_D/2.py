def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    b = [0] * n
    b[0] = a[0] - 1
    for i in range(1, n):
        b[i] = a[i] - a[i - 1] - 1
    b.append(10 ** 18 - a[n - 1])
    c = [0] * (n + 1)
    c[0] = b[0]
    for i in range(1, n):
        c[i] = c[i - 1] + b[i]
    for i in range(q):
        if k[i] <= c[0]:
            print(k[i])
        else:
            l = 0
            r = n
            while r - l > 1:
                mid = (l + r) // 2
                if c[mid] >= k[i]:
                    r = mid
                else:
                    l = mid
            print(a[l] + k[i] - c[l])
