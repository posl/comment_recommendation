def f(n):
    n -= 1
    s = ''
    while n >= 0:
        s = chr(ord('a') + n % 26) + s
        n //= 26
        n -= 1
    return s
n = int(input())
print(f(n))
