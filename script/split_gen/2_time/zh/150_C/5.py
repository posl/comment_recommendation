def permutation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for i in range(n):
            for j in permutation(n-1):
                result.append(j[:i]+[n]+j[i:])
        return result
