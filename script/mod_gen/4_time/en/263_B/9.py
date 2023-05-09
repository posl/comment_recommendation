def generation(n, p):
    generation = 1
    while n > 1:
        generation += 1
        n = p[n - 2]
    return generation

if __name__ == '__main__':
    generation()