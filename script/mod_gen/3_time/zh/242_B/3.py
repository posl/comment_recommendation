def get_min_permutation(s):
    s = list(s)
    s.sort()
    return ''.join(s)

if __name__ == '__main__':
    get_min_permutation()