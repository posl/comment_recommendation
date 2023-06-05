def func(n):
    for i in range(1, n):
        if i % 2 == 0 and i % n == 0:
            return i
    return n * 2
print(func(999999999))
