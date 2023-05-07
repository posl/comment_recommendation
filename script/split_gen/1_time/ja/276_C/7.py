def next_permutation(l):
    # 1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    for k in range(len(l)-2, -1, -1):
        if l[k] < l[k+1]:
            break
    else:
        return False
    # 2. Find the largest index l greater than k such that a[k] < a[l].
    for l in range(len(l)-1, k, -1):
        if l[k] < l[l]:
            break
    # 3. Swap the value of a[k] with that of a[l].
    l[k], l[l] = l[l], l[k]
    # 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
    l[k+1:] = l[:k:-1]
    return True
