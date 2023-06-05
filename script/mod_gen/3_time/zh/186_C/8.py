def is_contain_7(num):
    if str(num).find('7') != -1:
        return True
    elif str(oct(num)).find('7') != -1:
        return True
    else:
        return False

if __name__ == '__main__':
    is_contain_7()