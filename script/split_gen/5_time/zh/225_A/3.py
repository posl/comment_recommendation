def permutation(n):
    if len(n) <= 1:
        return [n]
    else:
        result = []
        for i in range(len(n)):
            for j in permutation(n[:i] + n[i+1:]):
                result.append(n[i:i+1] + j)
        return result
