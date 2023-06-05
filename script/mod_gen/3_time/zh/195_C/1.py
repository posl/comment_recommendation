def get_comma_count(n):
    n_str = str(n)
    n_len = len(n_str)
    comma_count = 0
    if n_len <= 3:
        return comma_count
    else:
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        # 从右边开始，每隔三个数字就用一个逗号
        if n_len % 3 == 0:
            comma_count = n_len // 3 - 1
        else:
            comma_count = n_len // 3
    return comma_count

if __name__ == '__main__':
    get_comma_count()