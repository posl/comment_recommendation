def is_contain_7(num):
    if num % 10 == 7:
        return True
    elif num > 10:
        return is_contain_7(num // 10)
    else:
        return False

if __name__ == '__main__':
    is_contain_7()