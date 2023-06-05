def permutate(s):
    if len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[1] + s[0]]
    else:
        result = []
        for i in range(len(s)):
            for j in permutate(s[:i] + s[i + 1:]):
                result.append(s[i] + j)
        return result
