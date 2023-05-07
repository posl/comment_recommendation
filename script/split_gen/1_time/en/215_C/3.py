def permutations(string):
    if len(string) == 1:
        return [string]
    else:
        perm_list = []
        for i in range(len(string)):
            char = string[i]
            remaining = string[:i] + string[i+1:]
            for perm in permutations(remaining):
                perm_list.append(char + perm)
        return perm_list
