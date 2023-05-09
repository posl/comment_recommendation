def check(num):
    if num % 2 == 1:
        return False
    elif num % 3 == 0:
        return True
    elif num % 5 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    check()