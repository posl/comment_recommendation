def problem214_a(n):
    if n <= 125:
        return 4
    elif n >= 126 and n <= 211:
        return 6
    else:
        return 8
