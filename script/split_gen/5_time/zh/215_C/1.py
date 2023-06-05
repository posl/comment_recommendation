def get_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for j in get_permutations(s[:i]+s[i+1:]):
                result.append(s[i]+j)
        return result
