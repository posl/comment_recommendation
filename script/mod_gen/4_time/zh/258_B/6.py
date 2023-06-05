def get_max_num(n, nums):
    max_num = 0
    for i in range(n):
        for j in range(n):
            tmp = get_max_num_by_start(n, nums, i, j)
            if tmp > max_num:
                max_num = tmp
    return max_num

if __name__ == '__main__':
    get_max_num()