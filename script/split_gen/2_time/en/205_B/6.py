def checkPermutation(n, seq):
    seq.sort()
    for i in range(n):
        if seq[i] != i+1:
            return "No"
    return "Yes"
