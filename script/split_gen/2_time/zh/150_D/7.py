def get_permutation_index(perm):
    """Return the index of the permutation in the lexicographic order."""
    perm = list(perm)
    perm = [x - 1 for x in perm]  # adjust the index to start from 0
    index = 0
    factorial = 1
    for i in range(len(perm)):
        index += perm[-i - 1] * factorial
        factorial *= len(perm) - i - 1
    return index
