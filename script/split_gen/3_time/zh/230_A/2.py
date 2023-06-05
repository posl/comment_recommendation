def agc(n):
    if n < 10:
        return "00" + str(n)
    elif n < 100:
        return "0" + str(n)
    else:
        return str(n)
