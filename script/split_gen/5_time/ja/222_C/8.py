def janken(a, b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    elif (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
        return -1
