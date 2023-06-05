def get_permutation_num(permutation):
    permutation_num = 0
    for i in range(0, len(permutation)):
        permutation_num += permutation[i] * (10 ** (len(permutation) - i - 1))
    return permutation_num
