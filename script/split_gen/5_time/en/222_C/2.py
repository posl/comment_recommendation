def rps(t1, t2):
    if t1 == 'G':
        if t2 == 'C':
            return 1
        elif t2 == 'P':
            return 2
        else:
            return 0
    elif t1 == 'C':
        if t2 == 'P':
            return 1
        elif t2 == 'G':
            return 2
        else:
            return 0
    else:
        if t2 == 'G':
            return 1
        elif t2 == 'C':
            return 2
        else:
            return 0
