def f(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return f(n/2)
    else:
        return f((n-1)/2)
n = int(input())
