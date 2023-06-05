def get_permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in get_permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
    return perms
