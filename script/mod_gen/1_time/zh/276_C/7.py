def get_next_permutation(perm):
    n = len(perm)
    # 从后向前寻找第一个顺序对(i, i+1)，满足perm[i] < perm[i+1]
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i == -1:
        return None
    # 从后向前寻找第一个满足perm[i] < perm[j]的j
    j = n - 1
    while perm[i] >= perm[j]:
        j -= 1
    # 交换perm[i]和perm[j]
    perm[i], perm[j] = perm[j], perm[i]
    # 将perm[i+1:]翻转
    perm[i + 1:] = perm[i + 1:][::-1]
    return perm

if __name__ == '__main__':
    get_next_permutation()