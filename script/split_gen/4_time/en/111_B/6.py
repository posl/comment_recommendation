def abc111_b(n):
    while True:
        if len(set(str(n))) == 1:
            return n
        n += 1
