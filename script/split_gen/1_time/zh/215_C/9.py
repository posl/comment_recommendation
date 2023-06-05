def permutation(string, s, e):
    if s == e:
        return [string]
    else:
        res = []
        for i in range(s, e):
            string[s], string[i] = string[i], string[s]
            res += permutation(string, s+1, e)
            string[s], string[i] = string[i], string[s]
        return res
