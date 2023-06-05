def get_min_replaced_num(n, v):
    # 从左到右找到第一个不同的数
    for i in range(n):
        if v[i] != v[0]:
            break
    # 从右到左找到第一个不同的数
    for j in range(n-1, -1, -1):
        if v[j] != v[-1]:
            break
    # 如果i和j相遇，说明整个数组都是相同的数
    if i == j:
        return n // 2
    # 如果i和j相邻，说明只有两个数，且相邻的两个数相等
    if i + 1 == j:
        return n // 2
    # 如果i和j不相邻，说明有两个数，且不相等
    return n - j + i

if __name__ == '__main__':
    get_min_replaced_num()