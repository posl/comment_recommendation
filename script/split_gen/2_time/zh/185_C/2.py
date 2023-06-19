def cut_iron(L):
    if L == 12:
        return 1
    elif L == 13:
        return 12
    elif L == 14:
        return 36
    elif L == 15:
        return 108
    elif L == 16:
        return 324
    elif L == 17:
        return 972
    else:
        return 3*cut_iron(L-1) - 3*cut_iron(L-2) + cut_iron(L-3)
