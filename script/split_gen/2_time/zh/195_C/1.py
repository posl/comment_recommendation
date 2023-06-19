def f(n):
    s = str(n)
    if len(s) <= 3:
        return 0
    if len(s) % 3 == 0:
        return len(s) // 3 - 1
    else:
        return len(s) // 3
