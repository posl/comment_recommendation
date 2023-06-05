def solve(n, a):
    b = [0] * n
    for i in range(0, n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    return b
n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a))
