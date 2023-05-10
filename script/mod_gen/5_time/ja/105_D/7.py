def get_num_divisible_by_m(num, m):
    if num < m:
        return 0
    else:
        return num // m

if __name__ == '__main__':
    get_num_divisible_by_m()