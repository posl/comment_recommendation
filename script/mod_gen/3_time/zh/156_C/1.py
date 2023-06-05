def min_energy(n, x):
    min_e = 100000
    for i in range(1, 101):
        e = 0
        for j in range(n):
            e += (x[j] - i) ** 2
        if e < min_e:
            min_e = e
    return min_e
n = int(input())
x = [int(i) for i in input().split()]
print(min_energy(n, x))
