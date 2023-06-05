def permutation(S):
    if len(S) == 1:
        return [S]
    else:
        res = []
        for i in range(len(S)):
            res += [S[i] + x for x in permutation(S[:i] + S[i+1:])]
        return res
