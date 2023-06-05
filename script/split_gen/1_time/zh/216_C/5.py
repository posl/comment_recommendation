def f(n):
    if n == 0:
        return ''
    if n % 2 == 0:
        return f((n - 2) // 2) + 'b'
    else:
        return f((n - 1) // 2) + 'a'
n = int(input())
print(f(n))
