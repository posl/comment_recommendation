def check753(num):
    if num < 10:
        if num == 7 or num == 5 or num == 3:
            return True
        else:
            return False
    else:
        if num % 10 == 7:
            return check753(num // 10)
        elif num % 10 == 5:
            return check753(num // 10)
        elif num % 10 == 3:
            return check753(num // 10)
        else:
            return False

if __name__ == '__main__':
    check753()