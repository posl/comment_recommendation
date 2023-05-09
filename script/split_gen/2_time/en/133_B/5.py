def distance(x1,x2):
    dist = 0
    for i in range(len(x1)):
        dist += (x1[i] - x2[i])**2
    return dist**(1/2)
