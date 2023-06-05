def cube_root(n):
    x = 0
    while x**3 < n:
        x += 1
    return x
