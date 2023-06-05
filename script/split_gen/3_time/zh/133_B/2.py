def calc_distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return int(sum**0.5)
