def exchange(num):
    num = str(num)
    num = num.replace('1','a')
    num = num.replace('9','1')
    num = num.replace('a','9')
    return int(num)

if __name__ == '__main__':
    exchange()