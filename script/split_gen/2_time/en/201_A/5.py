def is_arithmetic_sequence(a, b, c):
    if a == b and b == c:
        return True
    elif a == b or b == c or a == c:
        return False
    else:
        return (a - b) == (b - c)
