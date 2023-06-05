def print_sequence(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        start = 1
        if len(seq) > 0:
            start = seq[-1] + 1
        for i in range(start, m + 1):
            seq.append(i)
            print_sequence(n, m, seq)
            seq.pop()
