def calculate_total_power(x, p):
    total_power = 0
    for i in range(len(x)):
        total_power = total_power + (x[i] - p) ** 2
    return total_power
