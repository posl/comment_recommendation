def min_total_power(N, X):
    min_total_power = 0
    for i in range(1, 101):
        total_power = 0
        for j in range(N):
            total_power += (X[j] - i) ** 2
        if i == 1:
            min_total_power = total_power
        else:
            if total_power < min_total_power:
                min_total_power = total_power
    return min_total_power
