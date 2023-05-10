def calc(a,b):
    if b == 1:
        return 0
    else:
        return int((b-1)/(a-1))+1

if __name__ == '__main__':
    calc()