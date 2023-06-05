def getGeneration(n, p):
    maxGeneration = 0
    for i in range(1, n + 1):
        generation = 1
        parent = p[i - 1]
        while parent != -1:
            generation += 1
            parent = p[parent - 1]
        if generation > maxGeneration:
            maxGeneration = generation
    return maxGeneration
