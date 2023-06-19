def getYear(x):
    year = 0
    sum = 100
    while sum < x:
        sum = sum + int(sum * 0.01)
        year += 1
    return year
