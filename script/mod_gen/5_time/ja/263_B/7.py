def calc_generation(n,p):
    generation = 0
    while n != 1:
        generation += 1
        n = p[n-1]
    return generation

if __name__ == '__main__':
    calc_generation()