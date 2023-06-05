def permute(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i, c in enumerate(s):
        for p in permute(s[:i] + s[i+1:]):
            permutations.append(c + p)
    return permutations
S = input()
print(len(permute(S)))
