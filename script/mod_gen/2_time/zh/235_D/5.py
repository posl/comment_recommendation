def f(a, n):
    if n % a != 0:
        return -1
    m = n // a
    ans = 1
    while m > 1:
        if m % a == 0:
            m //= a
        elif m % a == 1:
            m = (m - 1) // a
        else:
            return -1
        ans += 1
    return ans
a, n = map(int, input().split())
print(f(a, n))
