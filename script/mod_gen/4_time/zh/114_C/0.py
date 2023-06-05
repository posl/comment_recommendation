def is753Number(num):
    numStr = str(num)
    if numStr.count('7') > 0 and numStr.count('5') > 0 and numStr.count('3') > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is753Number()