def is_contain_seven(n):
    if n%10 == 7:
        return True
    elif n//10 == 0:
        return False
    else:
        return is_contain_seven(n//10)
