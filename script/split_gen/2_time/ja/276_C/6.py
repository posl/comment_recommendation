def next_permutation(L):
    if len(L) == 1:
        return False
    i = len(L) - 1
    while i > 0 and L[i-1] >= L[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(L) - 1
    while L[j] <= L[i-1]:
        j -= 1
    L[i-1], L[j] = L[j], L[i-1]
    j = len(L) - 1
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    return True
