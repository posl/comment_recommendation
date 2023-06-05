def jumpable(n, x, a, b):
    if x == 0:
        return True
    if n == 0:
        return False
    if jumpable(n-1, x-a[n-1], a, b) or jumpable(n-1, x-b[n-1], a, b):
        return True
    return False
