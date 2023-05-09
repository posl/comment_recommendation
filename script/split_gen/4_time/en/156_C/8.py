def min_total_stamina(ppl,coords):
    if ppl == 1:
        return 0
    if ppl == 2:
        return abs(coords[0]-coords[1])
    min_stamina = 0
    for i in range(min(coords),max(coords)+1):
        stamina = 0
        for j in coords:
            stamina += (i-j)**2
        if stamina < min_stamina or min_stamina == 0:
            min_stamina = stamina
    return min_stamina
