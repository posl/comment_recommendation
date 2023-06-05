def is_even_digit(n):
    """
    判断一个数是否是偶数位
    :param n:
    :return:
    """
    str_n = str(n)
    if len(str_n) % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    is_even_digit()