def get_next_num(num):
    last_num = num % 10
    if last_num == 0:
        return num * 10 + 1
    elif last_num == 9:
        return num * 10 + 8
    else:
        return num * 10 + last_num - 1, num * 10 + last_num + 1

if __name__ == '__main__':
    get_next_num()