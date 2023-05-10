def find_multiple(a, b, c):
    for i in range(a, b+1):
        if i % c == 0:
            return i
    return -1
