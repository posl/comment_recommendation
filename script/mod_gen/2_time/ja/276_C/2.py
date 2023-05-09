def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i - 1] >= seq[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(seq) - 1
    while seq[j] <= seq[i - 1]:
        j -= 1
    seq[i - 1], seq[j] = seq[j], seq[i - 1]
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    next_permutation()