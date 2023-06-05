def problem206_b(n):
    i = 1
    while True:
        if n <= i*(i+1)/2:
            break
        else:
            i += 1
    return i
