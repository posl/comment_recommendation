def is_middle(a,b,c):
    if b < a:
        if b > c:
            return True
    if b > a:
        if b < c:
            return True
    return False
