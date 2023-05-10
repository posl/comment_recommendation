def janken(a, b):
    if a == b:
        return 0
    if a == "G":
        if b == "C":
            return 1
        if b == "P":
            return -1
    if a == "C":
        if b == "P":
            return 1
        if b == "G":
            return -1
    if a == "P":
        if b == "G":
            return 1
        if b == "C":
            return -1

if __name__ == '__main__':
    janken()