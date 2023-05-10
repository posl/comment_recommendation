def calculate_stamina(n, x):
    min_stamina = 100000000000
    for i in range(1, 101):
        stamina = 0
        for j in x:
            stamina += (j - i)**2
        if stamina < min_stamina:
            min_stamina = stamina
    return min_stamina
