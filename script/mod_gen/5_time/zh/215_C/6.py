def permutation(s):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in permutation(s[:i] + s[i+1:]):
            sl.append(s[i] + j)
    return sl

if __name__ == '__main__':
    permutation()