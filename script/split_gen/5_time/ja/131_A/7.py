def check_num(num):
    if num[0] == num[1] and num[1] == num[2]:
        return True
    elif num[1] == num[2] and num[2] == num[3]:
        return True
    else:
        return False
