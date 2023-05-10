def judge(a,b):
    if a == b:
        return 0
    elif a == "G":
        if b == "C":
            return 1
        elif b == "P":
            return -1
    elif a == "C":
        if b == "P":
            return 1
        elif b == "G":
            return -1
    elif a == "P":
        if b == "G":
            return 1
        elif b == "C":
            return -1
