def is753(num):
    num_str = str(num)
    if num_str.count('7') > 0 and num_str.count('5') > 0 and num_str.count('3') > 0:
        return True
    else:
        return False
