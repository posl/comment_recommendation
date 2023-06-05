def print_sequence(n, m, sequence):
    if len(sequence) == n:
        print(" ".join(map(str, sequence)))
    else:
        for i in range(1, m + 1):
            if i not in sequence:
                print_sequence(n, m, sequence + [i])
