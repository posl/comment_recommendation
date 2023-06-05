def print_seq(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, m+1):
        if len(seq) == 0 or i > seq[-1]:
            print_seq(n, m, seq + [i])
