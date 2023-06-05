def get_permutation(s, k):
    s = list(s)
    s.sort()
    k = k - 1
    result = []
    for i in range(len(s) - 1, -1, -1):
        j = k // factorial(i)
        k = k % factorial(i)
        result.append(s[j])
        del s[j]
    return ''.join(result)
