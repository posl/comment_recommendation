def min_energy(n, x):
    min_energy = 100000000
    for i in range(1, 101, 1):
        energy = 0
        for j in range(n):
            energy += (x[j] - i) ** 2
        if energy < min_energy:
            min_energy = energy
    return min_energy
n = int(input())
x = list(map(int, input().split()))
print(min_energy(n, x))
