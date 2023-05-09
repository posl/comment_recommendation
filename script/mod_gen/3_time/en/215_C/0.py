def next_permutation(s):
    s = list(s)
    i = len(s) - 1
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1
    if i <= 0:
        return ''.join(s)
    j = len(s) - 1
    while s[j] <= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = s[len(s) - 1: i - 1: -1]
    return ''.join(s)

if __name__ == '__main__':
    next_permutation()