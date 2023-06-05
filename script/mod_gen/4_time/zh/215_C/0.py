def permutation(s, k):
    if len(s) == 1:
        return s
    n = len(s)
    c = 1
    for i in range(1, n):
        c *= i
    q = int((k - 1) / c)
    r = k - c * q
    return s[q] + permutation(s[:q] + s[q+1:], r)

if __name__ == '__main__':
    permutation()