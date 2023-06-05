def judge(a,b):
    if a == 'G':
        if b == 'C':
            return 1
        elif b == 'P':
            return -1
        else:
            return 0
    elif a == 'C':
        if b == 'P':
            return 1
        elif b == 'G':
            return -1
        else:
            return 0
    else:
        if b == 'G':
            return 1
        elif b == 'C':
            return -1
        else:
            return 0

if __name__ == '__main__':
    judge()