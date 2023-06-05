def min_sum_power(n, x):
    min_power = 10000
    for i in range(1, 101):
        power = 0
        for j in range(n):
            power += (x[j] - i) ** 2
        if power < min_power:
            min_power = power
    return min_power
