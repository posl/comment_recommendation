def get_min_energy(n, x):
    # n: 人数
    # x: 坐标
    min_energy = 0
    for i in range(1, 101):
        energy = 0
        for j in range(n):
            energy += (x[j] - i)**2
        if i == 1:
            min_energy = energy
        else:
            if energy < min_energy:
                min_energy = energy
    return min_energy
