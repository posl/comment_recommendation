def min_stamina(n, x):
    min_stamina = 1000000000
    for i in range(1, 101):
        stamina = 0
        for j in range(n):
            stamina += (x[j] - i) ** 2
        if stamina < min_stamina:
            min_stamina = stamina
    return min_stamina
n = int(input())
x = list(map(int, input().split()))
print(min_stamina(n, x))
