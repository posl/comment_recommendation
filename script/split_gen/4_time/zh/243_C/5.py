def isCollision(a, b):
    if a[0] > b[0]:
        a, b = b, a
    if a[1] == b[1]:
        return True
    if a[1] > b[1]:
        return False
    if a[0] + a[1] > b[0] + b[1]:
        return False
    return True
