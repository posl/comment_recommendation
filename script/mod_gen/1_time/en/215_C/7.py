def find_kth_permutation(s, k):
    from itertools import permutations
    return sorted(list(permutations(s)))[k-1]

if __name__ == '__main__':
    find_kth_permutation()