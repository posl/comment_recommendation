def count_generation(n, p):
    generation = [0 for i in range(n)]
    for i in range(1, n):
        generation[i] = generation[p[i-1]-1] + 1
    return generation[n-1]

if __name__ == '__main__':
    count_generation()