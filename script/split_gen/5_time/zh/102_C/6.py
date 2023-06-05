def solve(n, a):
    s = sum(a)
    b = (s - n * (n + 1) // 2) // n
    return sum(abs(a[i] - (b + i + 1)) for i in range(n))
