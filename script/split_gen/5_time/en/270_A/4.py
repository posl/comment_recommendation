def problem270_a(a,b):
    c = 0
    if a > 0 and b > 0:
        c = 3 - a - b
    elif a > 0 and b == 0:
        c = 3 - a
    elif a == 0 and b > 0:
        c = 3 - b
    return c
