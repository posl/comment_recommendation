def check(num):
    num = str(num)
    for i in range(len(num)-1):
        if abs(int(num[i]) - int(num[i+1])) > 1:
            return False
    return True
