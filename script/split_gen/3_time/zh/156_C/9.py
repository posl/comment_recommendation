def min_energy(n, x):
    min = 1000000000000000000000000
    for p in range(1, 101):
        energy = 0
        for i in range(0, n):
            energy += (x[i] - p) ** 2
        if energy < min:
            min = energy
    return min
n = int(input())
x = list(map(int, input().split()))
print(min_energy(n, x))
