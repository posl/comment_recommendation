def get_max_num(n, a_list):
    a_list.sort(reverse=True)
    num = 0
    for i in a_list:
        num += i * 10**(i-1)
    return num
