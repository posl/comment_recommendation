def generation(N, p):
    generation = 0
    for i in range(N):
        generation += 1
        if p[i] == 1:
            break
        generation += generation(p[i]-1, p)
    return generation
