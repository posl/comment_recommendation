def replace_by_x(s):
    """
    用x替换字符串s中的每个字符
    :param s: 字符串
    :return: 替换后的字符串
    """
    result = ''
    for i in range(len(s)):
        result += 'x'
    return result

if __name__ == '__main__':
    replace_by_x()