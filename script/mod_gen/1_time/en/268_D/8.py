def get_permutations(s):
    if len(s) == 1:
        return s
    else:
        permutations = []
        for i in range(len(s)):
            for p in get_permutations(s[:i] + s[i+1:]):
                permutations.append(s[i] + p)
        return permutations

if __name__ == '__main__':
    get_permutations()