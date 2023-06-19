def problem102_a(n):
    i = 1
    while True:
        if i % 2 == 0 and i % n == 0:
            break
        i += 1
    return i
