def power2(n):
    if n == 0:
        return 1
    else:
        return 2 * power2(n-1)
