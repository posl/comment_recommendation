def get_total_sequences(n):
    total_sequences = 0
    for i in range(n):
        s = input()
        total_sequences += int(s.split()[0])
    return total_sequences
