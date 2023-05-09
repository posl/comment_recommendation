def check_if_approved_or_not(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False
    else:
        return True

if __name__ == '__main__':
    check_if_approved_or_not()