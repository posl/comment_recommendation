def min_sum_energy(n, x_list):
    min_energy = 10000000
    for i in range(1, 101):
        energy = 0
        for x in x_list:
            energy += (x - i)**2
        if energy < min_energy:
            min_energy = energy
    return min_energy

if __name__ == '__main__':
    min_sum_energy()