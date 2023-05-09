def next_permutation(p):
    i = len(p) - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(p) - 1
    while p[j] <= p[i-1]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p) - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    next_permutation()