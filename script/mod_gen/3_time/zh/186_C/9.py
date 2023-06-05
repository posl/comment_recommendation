def is_7_in_num(num, base=10):
    if base == 10:
        return str(num).find('7') >= 0
    elif base == 8:
        while num > 0:
            if num % 8 == 7:
                return True
            num //= 8
        return False

if __name__ == '__main__':
    is_7_in_num()