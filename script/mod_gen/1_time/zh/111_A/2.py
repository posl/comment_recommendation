def swap(num):
    num = str(num)
    num = num.replace('1','x')
    num = num.replace('9','1')
    num = num.replace('x','9')
    return num

if __name__ == '__main__':
    swap()