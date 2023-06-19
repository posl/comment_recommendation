def permutation(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        for j in permutation(s[:i] + s[i + 1:]):
            result.append(s[i] + j)
    return result
