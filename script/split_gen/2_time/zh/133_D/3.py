def solve(n, a):
    b = [0] * n
    for i in xrange(n):
        if i % 2 == 0:
            b[0] += a[i]
            b[1] -= a[i]
        else:
            b[0] -= a[i]
            b[1] += a[i]
    for i in xrange(1, n - 1):
        b[i + 1] = 2 * a[i] - b[i]
    return b
n = int(raw_input())
a = map(int, raw_input().split())
print " ".join(map(str, solve(n, a)))
