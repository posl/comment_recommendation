def is_difference(a,b,c):
    if a == b and b != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and a != b:
        return True
    else:
        return False
