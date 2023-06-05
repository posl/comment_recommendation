def get_permutation(s, n, k):
    if n == 1:
        return s
    q, r = divmod(k, factorial(n - 1))
    return s[q] + get_permutation(s[:q] + s[q + 1:], n - 1, r)
