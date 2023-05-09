def is_arithmetic_sequence(a, b, c):
    if a - b == b - c:
        return True
    elif a - c == c - b:
        return True
    elif b - a == a - c:
        return True
    elif b - c == c - a:
        return True
    elif c - a == a - b:
        return True
    elif c - b == b - a:
        return True
    else:
        return False
a, b, c = map(int, input().split())
