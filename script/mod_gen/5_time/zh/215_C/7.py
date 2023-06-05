def get_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perm_list = []
        for i in range(len(s)):
            for perm in get_permutations(s[:i] + s[i+1:]):
                perm_list.append(s[i] + perm)
        return perm_list

if __name__ == '__main__':
    get_permutations()