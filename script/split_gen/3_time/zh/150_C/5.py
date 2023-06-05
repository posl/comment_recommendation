def get_permutations(n):
    if n == 1:
        return [[1]]
    else:
        permutations = []
        for i in range(n):
            for j in get_permutations(n - 1):
                permutations.append(j[:i] + [n] + j[i:])
        return permutations
