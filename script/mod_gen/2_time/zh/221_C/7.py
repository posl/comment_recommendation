def get_max_product(num):
    num = str(num)
    length = len(num)
    if length == 2:
        return int(num[0]) * int(num[1])
    elif length == 3:
        return int(num[0]) * int(num[1:]) if int(num[0]) > int(num[1]) else int(num[0]) * int(num[2])
    else:
        return int(num[0]) * int(num[1:]) if int(num[0]) > int(num[1]) else int(num[0]) * int(num[2:])

if __name__ == '__main__':
    get_max_product()