def nextConfusingTime(H,M):
    if H < 0 or H > 23 or M < 0 or M > 59:
        return "Invalid Time"
    if H == 0 and M == 0:
        return "00 00"
    if H == 23 and M == 59:
        return "01 10"
    if M == 59:
        if H == 20:
            return "21 00"
        elif H == 21:
            return "22 00"
        elif H == 22:
            return "23 00"
        else:
            return "0" + str(H+1) + " 00"
    if M == 58:
        if H == 20:
            return "21 01"
        elif H == 21:
            return "22 01"
        elif H == 22:
            return "23 01"
        else:
            return "0" + str(H+1) + " 01"
    if M == 57:
        if H == 20:
            return "21 02"
        elif H == 21:
            return "22 02"
        elif H == 22:
            return "23 02"
        else:
            return "0" + str(H+1) + " 02"
    if M == 56:
        if H == 20:
            return "21 03"
        elif H == 21:
            return "22 03"
        elif H == 22:
            return "23 03"
        else:
            return "0" + str(H+1) + " 03"
    if M == 55:
        if H == 20:
            return "21 04"
        elif H == 21:
            return "22 04"
        elif H == 22:
            return "23 04"
        else:
            return "0" + str(H+1) + " 04"
    if M == 54:
        if H == 20:
            return "21 05"
        elif H == 21:
            return "22 05"
        elif H == 22:
            return "23 05"
        else:
            return "0" + str(H+1) + " 05"
    if M == 53:
        if H == 20:
            return "21
