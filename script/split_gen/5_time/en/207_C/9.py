def check_interval(i,j):
    if t[i] == 1:
        if t[j] == 1:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] > l[j]:
                return True
            else:
                return False
    elif t[i] == 2:
        if t[j] == 1:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] > l[j]:
                return True
            else:
                return False
    elif t[i] == 3:
        if t[j] == 1:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] >= l[j]:
                return True
            else:
                return False
    elif t[i] == 4:
        if t[j] == 1:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] >= l[j]:
                return True
            else
