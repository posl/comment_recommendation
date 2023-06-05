def get_num(n):
    num = 0
    for i in range(1,n+1):
        if i < 10:
            num += 1
        else:
            if i % 10 == i // (10 ** (len(str(i)) - 1)):
                num += 1
    return num

if __name__ == '__main__':
    get_num()