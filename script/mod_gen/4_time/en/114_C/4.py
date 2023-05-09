def isShichiGoSan(number):
    number = str(number)
    if '7' in number and '5' in number and '3' in number:
        return True
    return False

if __name__ == '__main__':
    isShichiGoSan()