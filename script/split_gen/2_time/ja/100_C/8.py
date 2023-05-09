def calc(a):
    if a%2 == 0:
        return calc(a/2) + 1
    else:
        return 0
