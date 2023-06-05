def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        res = []
        for i in range(len(string)):
            for j in get_permutations(string[:i] + string[i+1:]):
                res.append(string[i] + j)
        return res
