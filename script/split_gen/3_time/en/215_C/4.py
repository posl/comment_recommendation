def getPermutations(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for p in getPermutations(s[:i] + s[i+1:]):
                result.append(s[i] + p)
        return result
s, k = input().split()
k = int(k)
permutations = getPermutations(s)
permutations.sort()
print(permutations[k-1])
