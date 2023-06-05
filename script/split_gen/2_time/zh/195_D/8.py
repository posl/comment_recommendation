def get_comma_num(num):
    result = 0
    num_list = [int(i) for i in str(num)]
    num_len = len(num_list)
    for i in range(1, num_len):
        if i % 3 == 0:
            result += 1
    return result
