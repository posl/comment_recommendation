def check_str(str):
    if len(str) != 2:
        return False
    if str[0] not in 'HDCS':
        return False
    if str[1] not in 'A23456789TJQK':
        return False
    return True
