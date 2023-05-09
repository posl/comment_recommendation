def generate_sequence(n):
    if n == 1:
        return [1]
    else:
        sequence = generate_sequence(n-1)
        return sequence + [n] + sequence
