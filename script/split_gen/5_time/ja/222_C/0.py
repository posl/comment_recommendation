def janken(a, b):
    if a == b:
        return 0
    elif a == "G":
        if b == "C":
            return 1
        else:
            return -1
    elif a == "C":
        if b == "P":
            return 1
        else:
            return -1
    else:
        if b == "G":
            return 1
        else:
            return -1
