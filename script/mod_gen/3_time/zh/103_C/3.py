def get_max_f(num_list):
    max_num = max(num_list)
    num_list.remove(max_num)
    max_f = 0
    for i in range(max_num):
        f = 0
        for num in num_list:
            f += i%num
        if f > max_f:
            max_f = f
    return max_f

if __name__ == '__main__':
    get_max_f()