def is_triple_double(x, y, z):
    if x == y and x != z:
        return True
    elif x == z and x != y:
        return True
    elif y == z and y != x:
        return True
    else:
        return False
