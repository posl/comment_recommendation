def max_num(num_list):
    max_num = 0
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    max_num()