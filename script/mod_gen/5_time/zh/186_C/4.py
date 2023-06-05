def is7(num):
    if num % 7 == 0:
        return True
    while num != 0:
        if num % 10 == 7:
            return True
        num = num // 10
    return False

if __name__ == '__main__':
    is7()