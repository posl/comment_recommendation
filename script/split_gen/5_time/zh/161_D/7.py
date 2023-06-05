def get_next_num(num):
    if num == 0:
        return 1
    if num % 10 == 0:
        return num + 1
    if num % 10 == 9:
        return num - 1
    return num - 1
