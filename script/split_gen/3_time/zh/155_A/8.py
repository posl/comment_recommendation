def is_diff(a, b, c):
    if a == b and b != c:
        return True
    elif b == c and c != a:
        return True
    elif c == a and a != b:
        return True
    else:
        return False
