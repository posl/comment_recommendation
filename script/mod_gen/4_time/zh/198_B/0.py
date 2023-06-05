def isHuiwen(str):
    length = len(str)
    for i in range(length/2):
        if str[i] != str[length-1-i]:
            return False
    return True

if __name__ == '__main__':
    isHuiwen()