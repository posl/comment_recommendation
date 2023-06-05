def count_bottoms(s):
    """
    计算字符串s中的底的数量
    :param s: 一个由v和w组成的字符串
    :return: 底的数量
    """
    if len(s) == 1:
        return 1 if s == 'v' else 0
    else:
        return count_bottoms(s[0]) + count_bottoms(s[1:])

if __name__ == '__main__':
    count_bottoms()