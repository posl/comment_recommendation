def increasing_sequence(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [ [i] + s for i in range(1, m + 1) for s in increasing_sequence(n - 1, i - 1)]
