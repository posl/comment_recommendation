def judge(a,b):
    if a == "G":
        if b == "C":
            return True
        else:
            return False
    elif a == "C":
        if b == "P":
            return True
        else:
            return False
    else:
        if b == "G":
            return True
        else:
            return False
