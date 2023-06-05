def isLunLun(num):
    num = str(num)
    for i in range(1, len(num)):
        if abs(int(num[i-1]) - int(num[i])) > 1:
            return False
    return True
