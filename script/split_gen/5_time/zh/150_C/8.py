def permutationNumber(a):
    if len(a) == 1:
        return 1
    else:
        return len(a) * permutationNumber(a[1:])
