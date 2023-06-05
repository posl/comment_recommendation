def isLucky(num):
    num = str(num)
    for i in range(1, len(num)):
        if abs(int(num[i]) - int(num[i-1])) > 1:
            return False
    return True

if __name__ == '__main__':
    isLucky()