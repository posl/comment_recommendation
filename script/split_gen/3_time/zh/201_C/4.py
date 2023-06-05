def getPinCount(S):
    # 从S中获取o和x的个数
    S_list = list(S)
    o_count = S_list.count('o')
    x_count = S_list.count('x')
    # 从S中获取?的个数
    question_mark_count = S_list.count('?')
    # 获取S中o和x的位置
    o_index_list = []
    for i in range(len(S_list)):
        if S_list[i] == 'o':
            o_index_list.append(i)
    # 获取S中?的位置
    question_mark_index_list = []
    for i in range(len(S_list)):
        if S_list[i] == '?':
            question_mark_index_list.append(i)
    # 初始化密码个数
    pin_count = 0
    # 从o和x的位置中获取两个位置组成pin
    if o_count + x_count >= 4:
        for i in range(o_count + x_count - 3):
            for j in range(i + 1, o_count + x_count - 2):
                for k in range(j + 1, o_count + x_count - 1):
                    for l in range(k + 1, o_count + x_count):
                        # 获取pin
                        pin = [o_index_list[i], o_index_list[j], o_index_list[k], o_index_list[l]]
                        # 判断pin是否符合?的位置
                        flag = True
                        for index in question_mark_index_list:
                            if index not in pin:
                                flag = False
                                break
                        if flag:
                            pin_count += 1
    return pin_count
