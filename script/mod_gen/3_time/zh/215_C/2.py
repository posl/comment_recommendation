def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i, c in enumerate(s):
            result += [c + p for p in permutation(s[:i] + s[i+1:])]
        return result

if __name__ == '__main__':
    permutation()