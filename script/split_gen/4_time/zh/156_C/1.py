def get_min_energy(n, x):
    min_energy = 10000000
    for i in range(1, 101):
        energy = 0
        for j in range(n):
            energy += (x[j] - i) ** 2
        if energy < min_energy:
            min_energy = energy
    return min_energy
