def calDistance(x,y):
    import math
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return math.sqrt(sum)
