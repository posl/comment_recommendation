def isLunlun(num):
    if len(num) < 2:
        return True
    if abs(int(num[0]) - int(num[1])) > 1:
        return False
    return isLunlun(num[1:])

if __name__ == '__main__':
    isLunlun()