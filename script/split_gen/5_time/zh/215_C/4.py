def get_permutation(s, k):
    from itertools import permutations
    perm = sorted(set(permutations(s)))
    if k > len(perm):
        return 'None'
    else:
        return ''.join(perm[k-1])
