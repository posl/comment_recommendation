def find_smaller_permutation(p):
    # 找到下一个最小的排列组合
    # 从右到左找到第一个不是升序的数字
    # 该数字左边的数字都是升序的
    # 从右到左找到第一个比该数字大的数字
    # 交换这两个数字
    # 将该数字右边的数字按升序排列
    # 返回排列组合
    p = list(p)
    for i in range(len(p)-2, -1, -1):
        if p[i] < p[i+1]:
            break
    for j in range(len(p)-1, i, -1):
        if p[j] > p[i]:
            break
    p[i], p[j] = p[j], p[i]
    return p[:i+1] + sorted(p[i+1:])

if __name__ == '__main__':
    find_smaller_permutation()