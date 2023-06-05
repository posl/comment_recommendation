def is_permutation(n, seq):
    if n != len(seq):
        return False
    seq.sort()
    if seq[0] != 1:
        return False
    for i in range(1, n):
        if seq[i] - seq[i - 1] != 1:
            return False
    return True
n = int(input())
seq = list(map(int, input().split()))
