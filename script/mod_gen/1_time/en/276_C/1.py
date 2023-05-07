def next_permutation(p):
    n = len(p)
    i = n - 1
    while i > 0 and p[i - 1] >= p[i]:
        i -= 1
    if i <= 0:
        return False
    j = i - 1
    k = n - 1
    while k > j and p[j] >= p[k]:
        k -= 1
    p[j], p[k] = p[k], p[j]
    l = j + 1
    r = n - 1
    while l < r:
        p[l], p[r] = p[r], p[l]
        l += 1
        r -= 1
    return True

if __name__ == '__main__':
    next_permutation()