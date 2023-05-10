def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = [i for i in range(r)]
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1,r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

if __name__ == '__main__':
    combinations()