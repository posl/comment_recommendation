def isIncludeSeven(num):
    numStr = str(num)
    for i in numStr:
        if i == '7':
            return True
    return False

if __name__ == '__main__':
    isIncludeSeven()