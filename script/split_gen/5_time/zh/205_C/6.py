def compare_pow(a, b, c):
    if a == b:
        return '='
    elif c % 2 == 0:
        return '>' if abs(a) > abs(b) else '<'
    elif c % 2 == 1:
        return '>' if a > b else '<'
