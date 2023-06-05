def get_next_num(num):
    #print("get_next_num: num = ", num)
    num_str = str(num)
    num_str_len = len(num_str)
    num_str_half_len = num_str_len // 2
    #print("num_str_len = ", num_str_len)
    #print("num_str_half_len = ", num_str_half_len)
    num_str_half_len_plus_one = num_str_half_len + 1
    #print("num_str_half_len_plus_one = ", num_str_half_len_plus_one)
    #print("num_str[:num_str_half_len_plus_one] = ", num_str[:num_str_half_len_plus_one])
    #print("num_str[num_str_half_len_plus_one:] = ", num_str[num_str_half_len_plus_one:])
    if num_str[num_str_half_len_plus_one:] == "":
        #print("num_str[num_str_half_len_plus_one:] == ''")
        num_str_half_len -= 1
        num_str_half_len_plus_one -= 1
        #print("num_str_half_len = ", num_str_half_len)
        #print("num_str_half_len_plus_one = ", num_str_half_len_plus_one)
    if num_str_half_len == 0:
        #print("num_str_half_len == 0")
        num_str = str(int(num_str[0]) + 1)
        num_str_len = len(num_str)
        #print("num_str = ", num_str)
        #print("num_str_len = ", num_str_len)
        #print("num_str_half_len = ", num_str_half_len)
        #print("num_str_half_len_plus_one = ", num_str_half_len_plus_one)
        if num_str_len == num_str_half_len_plus_one:
            #print("num_str_len == num_str_half_len_plus_one")
            num_str = "1" + "0" * num_str_len
        else:
            #print("num_str_len != num_str_half_len_plus_one")
            num_str = "1" + "0" * (num_str_len - 1)
        #print("num_str = ", num_str)
        num_str_len = len(num_str)
        num_str_half_len = num_str_len // 2
        num_str_half_len_plus_one = num_str_half_len + 1
        #print("num_str_len = ", num_str_len)
        #print("num_str_half_len =

if __name__ == '__main__':
    get_next_num()