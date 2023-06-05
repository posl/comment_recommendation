def getSumOfPower(x, p):
    sum = 0
    for i in x:
        sum += (i - p) ** 2
    return sum
