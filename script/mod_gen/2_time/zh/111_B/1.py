def replace_1_9(n):
    return int(str(n).replace('1', 'a').replace('9', '1').replace('a', '9'))

if __name__ == '__main__':
    replace_1_9()