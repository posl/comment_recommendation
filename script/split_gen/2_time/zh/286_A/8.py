def problems286_a():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i < p - 1:
            b[i + s - q] = a[i]
        elif i < r - 1:
            b[i - p + q] = a[i]
        else:
            b[i + s - r] = a[i]
    print(*b)
