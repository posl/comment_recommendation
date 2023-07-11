def isContainSeven(num):
    if num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7:
        return True
    else:
        return False

if __name__ == '__main__':
    isContainSeven()