def judge(num):
    if -2**31 <= num <= 2**31-1:
        return "是"
    else:
        return "否"
