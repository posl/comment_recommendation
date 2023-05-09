def isShichiGoSan(num):
    num_str = str(num)
    if '7' in num_str and '5' in num_str and '3' in num_str:
        return True
    else:
        return False
