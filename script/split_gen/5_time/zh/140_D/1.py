def cal_happy_num(str):
    happy_num = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            happy_num += 1
    return happy_num
