def is_seven(num):
    if '7' in str(num) or '7' in oct(num)[2:]:
        return True
    return False
