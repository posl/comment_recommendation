def next_permutation(s):
    # 1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    k = -1
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            k = i
    if k == -1:
        return False
    # 2. Find the largest index l greater than k such that a[k] < a[l].
    l = -1
    for i in range(k, len(s)):
        if s[k] < s[i]:
            l = i
    # 3. Swap the value of a[k] with that of a[l].
    s[k], s[l] = s[l], s[k]
    # 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
    s[k + 1:] = s[:k:-1]
    return True

if __name__ == '__main__':
    next_permutation()