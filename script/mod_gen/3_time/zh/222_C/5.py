def rps(a, b):
    if a == "G":
        if b == "G":
            return 0
        elif b == "C":
            return 1
        elif b == "P":
            return -1
    elif a == "C":
        if b == "G":
            return -1
        elif b == "C":
            return 0
        elif b == "P":
            return 1
    elif a == "P":
        if b == "G":
            return 1
        elif b == "C":
            return -1
        elif b == "P":
            return 0

if __name__ == '__main__':
    rps()