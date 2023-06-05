def get_min_change_num(str1, str2):
    """
    从str1中找出str2的最小子串，需要改变的字符数
    :param str1:
    :param str2:
    :return:
    """
    # 从str1中找出str2的最小子串，需要改变的字符数
    # 初始化
    min_change_num = 1000
    for i in range(len(str1)):
        print(i)
        for j in range(i+1, len(str1)):
            print(j)
            sub_str1 = str1[i:j]
            print(sub_str1)
            if str2 in sub_str1:
                print("str2 in sub_str1")
                change_num = len(sub_str1) - len(str2)
                if change_num < min_change_num:
                    min_change_num = change_num
    return min_change_num
