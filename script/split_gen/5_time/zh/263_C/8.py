def print_sequence(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        for i in range(1, m + 1):
            if len(seq) == 0 or i > seq[-1]:
                seq.append(i)
                print_sequence(n, m, seq)
                seq.pop()
