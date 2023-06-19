def problem257_a(n, x):
    for i in range(1, 27):
        if x <= i * n:
            return chr(65 + i - 1)
