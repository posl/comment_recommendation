def calc(a, b):
    if a >= b:
        return 1
    else:
        if b % a == 0:
            return b / a
        else:
            return b / a + 1
