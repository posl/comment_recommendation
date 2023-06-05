def get_min_power(x):
    min_power = 0
    for i in range(len(x)):
        min_power += (x[i] - 1)**2
    return min_power
