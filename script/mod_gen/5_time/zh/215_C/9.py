def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for j in permutation(s[:i] + s[i+1:]):
                res.append(s[i] + j)
        return res

if __name__ == '__main__':
    permutation()