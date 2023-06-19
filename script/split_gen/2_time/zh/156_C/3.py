def min_total_power(N, X):
    min_power = 10000000
    for i in range(1, 101):
        power = 0
        for j in range(N):
            power += (X[j] - i) ** 2
        if power < min_power:
            min_power = power
    return min_power
