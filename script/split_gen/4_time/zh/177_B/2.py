def find_min_change(s, t):
    # s = list(s)
    # t = list(t)
    # print(s)
    # print(t)
    # s_len = len(s)
    # t_len = len(t)
    # if s_len < t_len:
    #     return -1
    # else:
    #     min_change = 0
    #     for i in range(t_len):
    #         if s[i] != t[i]:
    #             min_change += 1
    #     return min_change
    s = list(s)
    t = list(t)
    s_len = len(s)
    t_len = len(t)
    if s_len < t_len:
        return -1
    else:
        min_change = 0
        for i in range(s_len - t_len + 1):
            for j in range(t_len):
                if s[i + j] != t[j]:
                    min_change += 1
        return min_change
