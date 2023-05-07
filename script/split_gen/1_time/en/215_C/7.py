def find_kth_permutation(s, k):
    from itertools import permutations
    return sorted(list(permutations(s)))[k-1]
