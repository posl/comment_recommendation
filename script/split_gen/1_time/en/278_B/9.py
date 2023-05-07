def nextConfusingTime(H, M):
    if H <= 1:
        if M <= 23:
            return [H, 23]
        else:
            return [H, 59]
    elif H <= 2:
        if M <= 13:
            return [H, 13]
        else:
            return [H, 59]
    elif H <= 3:
        if M <= 3:
            return [H, 3]
        else:
            return [H, 59]
    elif H <= 4:
        if M <= 43:
            return [H, 43]
        else:
            return [H, 59]
    elif H <= 5:
        if M <= 33:
            return [H, 33]
        else:
            return [H, 59]
    elif H <= 6:
        if M <= 23:
            return [H, 23]
        else:
            return [H, 59]
    elif H <= 7:
        if M <= 13:
            return [H, 13]
        else:
            return [H, 59]
    elif H <= 8:
        if M <= 3:
            return [H, 3]
        else:
            return [H, 59]
    elif H <= 9:
        if M <= 53:
            return [H, 53]
        else:
            return [H, 59]
    elif H <= 10:
        if M <= 43:
            return [H, 43]
        else:
            return [H, 59]
    elif H <= 11:
        if M <= 33:
            return [H, 33]
        else:
            return [H, 59]
    elif H <= 12:
        if M <= 23:
            return [H, 23]
        else:
            return [H, 59]
    elif H <= 13:
        if M <= 13:
            return [H, 13]
        else:
            return [H, 59]
    elif H <= 14:
        if M <= 3:
            return [H, 3]
        else:
            return [H, 59]
    elif H <= 15:
        if M <= 53:
            return [H, 53]
        else:
            return [H,
