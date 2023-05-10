def generate_sequences(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    seqs = []
    for i in range(1, m+1):
        for seq in generate_sequences(n-1, m):
            if seq[-1] < i:
                seqs.append(seq+[i])
    return seqs

if __name__ == '__main__':
    generate_sequences()