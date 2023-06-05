def get_min_max(s):
    s_list = list(s)
    min_s = s
    max_s = s
    for i in range(len(s)):
        s_list.append(s_list[0])
        s_list.remove(s_list[0])
        str_tmp = ''.join(s_list)
        if str_tmp < min_s:
            min_s = str_tmp
        if str_tmp > max_s:
            max_s = str_tmp
    return min_s, max_s

if __name__ == '__main__':
    get_min_max()