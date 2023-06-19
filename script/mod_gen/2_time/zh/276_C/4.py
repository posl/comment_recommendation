def find_min_permutation(n, p):
    # 1. find the largest i, s.t. p[i] > p[i-1]
    i = n - 1
    while i > 0:
        if p[i] > p[i-1]:
            break
        i -= 1
    # 2. find the largest j, s.t. p[j] > p[i-1]
    j = n - 1
    while j > i:
        if p[j] > p[i-1]:
            break
        j -= 1
    # 3. swap p[i-1] and p[j]
    p[i-1], p[j] = p[j], p[i-1]
    # 4. reverse p[i:]
    p[i:] = p[i:][::-1]
    return p

if __name__ == '__main__':
    find_min_permutation()