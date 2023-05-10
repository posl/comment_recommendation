def print_increasing_seq(n, m, seq):
    if len(seq) == n:
        print(" ".join([str(x) for x in seq]))
    else:
        if len(seq) == 0:
            start = 1
        else:
            start = seq[-1] + 1
        for i in range(start, m+1):
            seq.append(i)
            print_increasing_seq(n, m, seq)
            seq.pop()

if __name__ == '__main__':
    print_increasing_seq()