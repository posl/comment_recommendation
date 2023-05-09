def permutation(n):
    def perm(n, i, j):
        if i == j:
            yield n
        else:
            for k in range(i, j):
                n[i], n[k] = n[k], n[i]
                for x in perm(n, i + 1, j):
                    yield x
                n[i], n[k] = n[k], n[i]
    return perm(n, 0, len(n))
