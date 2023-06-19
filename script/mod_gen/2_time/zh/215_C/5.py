def permutation(s, k):
    s = sorted(s)
    return ''.join(s[k-1])

if __name__ == '__main__':
    permutation()