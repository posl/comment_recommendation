def cal(a):
    if a % 2 == 0:
        return a / 2
    elif a % 3 == 0:
        return a / 3
    else:
        return -1

if __name__ == '__main__':
    cal()