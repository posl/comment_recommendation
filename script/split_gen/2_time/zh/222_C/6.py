def check_win(p1,p2):
    if p1 == p2:
        return 0
    elif p1 == 'G' and p2 == 'C':
        return 1
    elif p1 == 'C' and p2 == 'P':
        return 1
    elif p1 == 'P' and p2 == 'G':
        return 1
    else:
        return -1
