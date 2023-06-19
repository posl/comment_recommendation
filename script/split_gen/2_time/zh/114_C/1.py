def check753(num):
    if num < 357:
        return False
    if num % 2 == 0:
        return False
    if num % 5 == 0:
        return False
    if num % 3 == 0:
        return False
    str_num = str(num)
    if "0" in str_num:
        return False
    if "1" in str_num:
        return False
    if "2" in str_num:
        return False
    if "4" in str_num:
        return False
    if "6" in str_num:
        return False
    if "8" in str_num:
        return False
    if "9" in str_num:
        return False
    return True
