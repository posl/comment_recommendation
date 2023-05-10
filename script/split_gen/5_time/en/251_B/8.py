def is_ok(a, w):
    if w <= 0:
        return False
    if a[0] == w or a[1] == w or a[2] == w:
        return True
    if w - a[0] < 0:
        return False
    if w - a[1] < 0:
        return False
    if w - a[2] < 0:
        return False
    if w - a[0] - a[1] < 0:
        return False
    if w - a[0] - a[2] < 0:
        return False
    if w - a[1] - a[2] < 0:
        return False
    if w - a[0] - a[1] - a[2] < 0:
        return False
    return True
