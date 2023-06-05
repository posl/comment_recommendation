def get_permutation(s):
    if len(s) == 1:
        return [s]
    else:
        permutations = []
        for i in range(len(s)):
            for j in get_permutation(s[:i] + s[i + 1:]):
                permutations.append(s[i] + j)
        return permutations
