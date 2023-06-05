def check(l):
    if len(l) % 2 != 0:
        return False
    if len(l) == 2:
        return False
    if len(l) == 4:
        if l[0] == l[2] and l[1] == l[3] and l[0] != l[1]:
            return True
        else:
            return False
    if len(l) > 4:
        if l[0] == l[2] and l[1] == l[3] and l[0] != l[1]:
            return check(l[2:])
        else:
            return False
