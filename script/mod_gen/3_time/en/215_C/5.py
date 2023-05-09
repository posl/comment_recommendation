def getPermutations(s):
    if len(s) == 1:
        return [s]
    else:
        permutations = []
        for i in range(len(s)):
            for perm in getPermutations(s[:i] + s[i+1:]):
                permutations.append(s[i] + perm)
        return permutations

if __name__ == '__main__':
    getPermutations()