def getGeneration(n, p):
    generation = 1
    for i in range(1, n):
        if p[i] == 1:
            generation += 1
        else:
            generation = getGeneration(p[i], p) + 1
    return generation
