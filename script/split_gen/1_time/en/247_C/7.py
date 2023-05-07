def print_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = print_sequence(n-1)
        return seq + [n] + seq
