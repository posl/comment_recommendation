def print_sequences(n, m, sequence):
    if n == 0:
        print(sequence)
        return
    for i in range(1, m + 1):
        print_sequences(n - 1, m, sequence + str(i))
