def calc_sum(x, p):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - p) ** 2
    return sum
