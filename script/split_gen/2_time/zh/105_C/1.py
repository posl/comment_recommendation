def convert_to_base2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num % 2 == 0:
        return convert_to_base2(num / (-2)) * 10
    else:
        return convert_to_base2((num - 1) / (-2)) * 10 + 1
