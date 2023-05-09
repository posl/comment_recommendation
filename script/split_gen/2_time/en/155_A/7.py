def poor(a,b,c):
    if a == b:
        if b == c:
            return False
        else:
            return True
    elif a == c:
        if b == c:
            return False
        else:
            return True
    elif b == c:
        if a == c:
            return False
        else:
            return True
    else:
        return False
