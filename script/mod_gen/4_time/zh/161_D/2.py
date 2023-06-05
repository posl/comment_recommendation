def check(num):
    num = str(num)
    if len(num) == 1:
        return True
    for i in range(len(num) - 1):
        if abs(int(num[i]) - int(num[i + 1])) > 1:
            return False
    return True

if __name__ == '__main__':
    check()