def check(a, b):
    if a == 0 and b == 0:
        return True
    if a == 0 or b == 0:
        return False
    if a == b:
        return False
    if a == 1 and b == 1:
        return False
    return True
