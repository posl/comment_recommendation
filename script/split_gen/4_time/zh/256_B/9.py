def problem256_b(n, a):
    p = 0
    for i in a:
        p += i // 4
    print(p)
