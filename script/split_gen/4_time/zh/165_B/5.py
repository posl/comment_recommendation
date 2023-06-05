def getYear(x):
    i = 0
    y = 100
    while y < x:
        y += int(y * 0.01)
        i += 1
    return i
