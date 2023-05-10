def check_shichigosan(number):
    str_number = str(number)
    if '7' in str_number and '5' in str_number and '3' in str_number:
        return True
    else:
        return False

if __name__ == '__main__':
    check_shichigosan()