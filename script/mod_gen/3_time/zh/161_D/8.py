def check(num):
    num = str(num)
    length = len(num)
    for i in range(length):
        if i == length-1:
            return True
        if abs(int(num[i])-int(num[i+1])) > 1:
            return False

if __name__ == '__main__':
    check()