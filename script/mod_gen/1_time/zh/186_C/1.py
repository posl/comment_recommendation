def is_contain_seven(num, base):
    while num > 0:
        if num % base == 7:
            return True
        num = num // base
    return False

if __name__ == '__main__':
    is_contain_seven()